# Generated by Django 5.1.3 on 2024-11-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='Опис відсутній'),
            preserve_default=False,
        ),
    ]
