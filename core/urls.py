from django.urls import path
from .views import (
    DoctorDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    checkout_success
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('booking/<int:pk>', CheckoutView.as_view(), name='booking'),
    path('checkout/success/', checkout_success, name='checkout-success'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
