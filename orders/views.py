# orders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.db import transaction
from cart.cart import Cart
from .models import Order, OrderItem
from .forms import CheckoutForm
import stripe # For credit_card payment
from decimal import Decimal

def to_decimal(value):
    """Convert any value to Decimal safely"""
    if isinstance(value, Decimal):
        return value
    if isinstance(value, (int, float)):
        return Decimal(str(value))
    if isinstance(value, str):
        return Decimal(value)
    return Decimal('0')

# You may also need to import an external PayPal library or custom module:
# import paypal_integration_module

# Initialize Stripe (Ensure this is at the top)
stripe.api_key = getattr(settings, 'STRIPE_SECRET_KEY', 'your-stripe-secret-key-here')

# --- 1. Order Creation/Checkout ---

@login_required
@transaction.atomic # Ensures database operations are atomized
def order_create(request):
    cart = Cart(request)
    
    if not cart:
        messages.warning(request, "Your cart is empty. Add some products first!")
        return redirect('cart:cart_detail')
    
    # --- Form Submission (POST) ---
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        
        if form.is_valid():
            # Calculate shipping cost based on method (Refined Logic)
            shipping_method = form.cleaned_data.get('shipping_method', 'standard')
            shipping_costs = {
                'express': 15.99, 
                'overnight': 29.99, 
                'standard': 5.99
            }
            shipping_cost = shipping_costs.get(shipping_method, 5.99)
            
            # Create order
            order = form.save(commit=False)
            order.user = request.user
            order.shipping_method = shipping_method
            order.shipping_cost = shipping_cost
            order.save()
            
            # Create order items and clear cart
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            
            # Redirect to payment based on selected method
            payment_method = form.cleaned_data['payment_method']
            
            if payment_method == 'credit_card':
                return redirect('orders:payment', order_id=order.id)
            elif payment_method == 'paypal':
                return redirect('orders:paypal_payment', order_id=order.id)
            else:
                # Handle Cash On Delivery/Bank Transfer (assuming instant confirmation)
                order.payment_status = 'pending' # Set status for non-instant payments
                order.save()
                messages.success(request, f'Order #{order.id} has been placed successfully, awaiting payment!')
                return redirect('orders:order_confirmation', order_id=order.id)
    
    # --- Initial Form Display (GET) ---
    else:
        # Pre-fill form with user data if available
        initial_data = {}
        if request.user.is_authenticated:
            # Safely get profile data
            initial_data = {
                'first_name': request.user.first_name or '',
                'last_name': request.user.last_name or '',
                'email': request.user.email or '',
            }
            try:
                profile = request.user.profile
                initial_data.update({
                    'phone': getattr(profile, 'phone', ''),
                    'address': getattr(profile, 'address', ''),
                    'city': getattr(profile, 'city', ''),
                    'state': getattr(profile, 'state', ''),
                    'postal_code': getattr(profile, 'postal_code', ''),
                })
            except AttributeError:
                 # Profile doesn't exist, ignore
                pass
        
        form = CheckoutForm(initial=initial_data)

    # Calculate totals for display
    subtotal = cart.get_total_price()
    # Use default shipping cost for display before form submission
    shipping_cost = Decimal('5.99') 
    tax_rate = Decimal('0.08')
    tax = subtotal * Decimal(str(tax_rate))
    total = subtotal + Decimal(str(shipping_cost)) + Decimal(str(tax))
    
    context = {
        'form': form,
        'cart': cart,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'tax': tax,
        'total': total,
        'tax_rate': tax_rate,
    }
    
    return render(request, 'orders/check_out.html', context)


# --- 2. Credit Card Payment (Stripe) ---

@login_required
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Logic to create a PaymentIntent is usually done on page load, 
    # and confirmation is handled via AJAX/webhook. 
    # The current code simulates a simple direct POST integration.
    
    if request.method == 'POST':
        # Process Stripe payment (simplified example, usually requires client-side JS)
        try:
            # The code snippet you provided only creates the intent, it doesn't confirm it.
            # In a real scenario, you'd use a payment token/method ID from the frontend.
            # This logic must be refined for a secure implementation.
            
            # Example for creating a PaymentIntent token to send to the template:
            intent = stripe.PaymentIntent.create(
                amount=int(order.get_total_cost() * 100),  # Convert to cents
                currency='usd',
                metadata={'order_id': order.id, 'user_id': request.user.id},
                description=f'Order #{order.id}',
            )
            
            # Assuming successful payment confirmation here for simplicity
            order.payment_status = 'paid'
            order.paid = True
            order.transaction_id = intent.id
            order.save()
            
            messages.success(request, f'Payment successful! Order #{order.id} has been confirmed.')
            return redirect('orders:order_confirmation', order_id=order.id)
            
        except stripe.error.StripeError as e:
            messages.error(request, f'Payment failed: {str(e)}')
            return redirect('orders:payment', order_id=order.id)
    
    # On GET request, prepare for payment (e.g., fetch client secret)
    try:
        # Create a fresh intent or retrieve an existing one
        intent = stripe.PaymentIntent.create(
            amount=int(order.get_total_cost() * 100),
            currency='usd',
            metadata={'order_id': order.id, 'user_id': request.user.id},
        )
    except Exception as e:
        messages.error(request, "Could not initialize payment intent.")
        return redirect('orders:order_detail', order_id=order.id)


    context = {
        'order': order,
        'stripe_public_key': getattr(settings, 'STRIPE_PUBLIC_KEY', 'your-stripe-public-key-here'),
        'client_secret': intent.client_secret, # Pass client secret for Stripe JS
    }
    
    return render(request, 'orders/payment.html', context)

# --- 3. PayPal Payment (Placeholder) ---

@login_required
@transaction.atomic
def paypal_payment(request, order_id):
    """
    Handles the initiation of the PayPal payment process.
    
    FIX: This view definition was MISSING from your provided code.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # --- PayPal Integration Logic ---
    
    # 1. Integrate with the PayPal SDK/API here.
    # 2. Typically, you create a PayPal Order and redirect the user to the PayPal site.
    
    messages.info(request, f"Redirecting to PayPal for Order #{order.id}...")
    
    # In a real application, you would return a redirect to the PayPal external link.
    # Example: return redirect(paypal_api.create_payment(order))
    
    # For now, we redirect back to the order detail page as a placeholder
    return redirect('orders:order_detail', order_id=order.id)


# --- 4. Confirmation, History, and Detail Views (Placeholders) ---

@login_required
def order_confirmation(request, order_id):
    """
    Final page displayed after a successful payment/order placement.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_confirmation.html', {'order': order})


@login_required
def order_history(request):
    """
    Lists all orders for the current logged-in user.
    """
    orders = Order.objects.filter(user=request.user).order_by('-created')
    return render(request, 'orders/history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """
    Displays the details of a single order.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/detail.html', {'order': order})