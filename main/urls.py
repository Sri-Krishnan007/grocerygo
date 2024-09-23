from django.urls import path
from . import views
from .views import product_list,Cart,checkout,order_history,product_detail

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('otp_verification/', views.otp_verification_view, name='otp_verification'),
    path('products/', product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('order_history/', views.order_history, name='order_history'),
    
]
