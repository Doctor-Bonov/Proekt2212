from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='Опис відсутній')  # Якщо поле опису порожнє, буде використовуватись це значення
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Поле для зображення

    def __str__(self):
        return self.name
