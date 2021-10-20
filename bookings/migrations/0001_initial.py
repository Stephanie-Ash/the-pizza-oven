# Generated by Django 3.2.7 on 2021-10-20 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0003_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField(default=datetime.time(18, 0))),
                ('end_time', models.TimeField(editable=False)),
                ('party_size', models.IntegerField(choices=[(1, '1 person'), (2, '2 people'), (3, '3 people'), (4, '4 people'), (5, '5 people'), (6, '6 people'), (7, '7 people'), (8, '8 people')], default=2)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('special_requirements', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('tables', models.ManyToManyField(blank=True, related_name='bookings', to='restaurant.Table')),
            ],
        ),
    ]
