# Generated by Django 3.2.7 on 2021-11-03 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_alter_booking_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='updated_on',
        ),
    ]