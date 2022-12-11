from django.urls import path
from .views import (
    DoctorDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    proceed_payment,
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
    path('bookings/<int:pk>', CheckoutView.as_view(), name='booking'),
    path('bookings/<int:pk>/proceed-payment', proceed_payment, name='booking-proceed-payment'),
    path('checkout/success/', checkout_success, name='checkout-success'),
    path('booking-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('doctor/<str:slug>/<int:pk>/', DoctorDetailView.as_view(), name='product'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
]
