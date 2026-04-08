from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('category/<str:drama_name>/', views.category_view),
    path('product/<int:product_id>/', views.product_detail),

    path('add-to-cart/<int:product_id>/', views.add_to_cart),
    path('cart/', views.cart_view),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart),

    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist),
    path('wishlist/', views.wishlist_view),
    path('remove-from-wishlist/<int:product_id>/', views.remove_from_wishlist),
    path('checkout/', views.checkout, name='checkout'),
    path('increase/<int:product_id>/', views.increase_quantity),
path('decrease/<int:product_id>/', views.decrease_quantity),
]