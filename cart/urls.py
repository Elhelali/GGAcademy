from django.urls import path, include
from . import views
import datetime, time, calendar


app_name= 'cart'




urlpatterns= [
path('add/<int:product_id>',views.add_cart, name='add_cart'),
path('', views.cart_detail, name='cart_detail'),
path('<carid>', views.cart_detail),
path('remove/<int:product_id>/<str:slot>', views.cart_remove, name='cart_remove'),
path('full_remove/<int:product_id>', views.full_remove, name='full_remove'),


]


	