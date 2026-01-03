# orders/urls.py
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.order_create, name='order_create'),
    path('payment/<int:order_id>/', views.payment, name='payment'),
    path('paypal/<int:order_id>/', views.paypal_payment, name='paypal_payment'),
    path('confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('history/', views.order_history, name='order_history'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
]