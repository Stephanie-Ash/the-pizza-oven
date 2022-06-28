# Generated by Django 3.2.7 on 2021-11-02 15:42

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('restaurant', '0004_alter_restaurant_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='menu',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
