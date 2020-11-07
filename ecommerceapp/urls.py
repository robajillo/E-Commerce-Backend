from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/products/', views.products_list),
    path('api/products/<int:pk>', views.product_detail),
    path('api/orders/', views.orders_list),
    path('api/orders/<int:pk>', views.order_detail),
    path('api/carts/', views.carts_list),
    path('api/carts/<int:pk>', views.cart_detail)
]