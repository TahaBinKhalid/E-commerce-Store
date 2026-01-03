from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'address', 'city', 'state', 'postal_code', 'country',
            'payment_method', 'notes'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name',
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Full Address',
                'rows': 3,
                'required': True
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City',
                'required': True
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'State/Province'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Postal/ZIP Code',
                'required': True
            }),
            'country': forms.Select(attrs={
                'class': 'form-control'
            }),
            'payment_method': forms.Select(attrs={
                'class': 'form-control'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Any special instructions or notes...',
                'rows': 3
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add Bootstrap classes to all fields
        for field in self.fields:
            if 'class' not in self.fields[field].widget.attrs:
                self.fields[field].widget.attrs.update({'class': 'form-control'})