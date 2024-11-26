# shop_project/urls.py

from django.contrib import admin
from django.urls import path, include  # Не забудь імпортувати include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # Підключаємо urls додатку shop
]

# Додаємо налаштування для медіафайлів
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
