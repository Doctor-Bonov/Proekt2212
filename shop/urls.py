# shop/urls.py

from django.urls import path
from . import views  # Імпортуємо views з поточного додатку

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Головна сторінка зі списком товарів
    path('<int:product_id>/', views.product_detail, name='product_detail'),  # Деталі товару
]
