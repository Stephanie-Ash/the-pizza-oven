# Generated by Django 3.2.7 on 2021-11-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('restaurant', '0009_alter_restaurant_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.TextField(blank=True,
                                   help_text='Warning editing this field will change theAbout Us section on the home page!Clear the field to display the default text.'),
        ),
    ]
