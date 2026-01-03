from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart

def cart_detail(request):
    cart = Cart(request)
    
    # Debug: print cart contents
    print("Cart session data:", cart.cart)
    
    return render(request, 'cart/detail.html', {'cart': cart})
    
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')
@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.update(product=product, quantity=quantity)  
    return redirect('cart:cart_detail')

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart

def cart_detail(request):
    cart = Cart(request)
    
    # Clean up any invalid products from the cart
    product_ids = list(cart.cart.keys())
    for product_id in product_ids:
        try:
            # Try to get the product
            product = Product.objects.get(id=int(product_id))
        except (Product.DoesNotExist, ValueError):
            # If product doesn't exist or ID is invalid, remove it from cart
            del cart.cart[product_id]
            cart.save()
    
    return render(request, 'cart/detail.html', {'cart': cart})