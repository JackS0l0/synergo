# Generated by Django 5.1.7 on 2025-03-13 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_services_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='banner',
            field=models.BooleanField(default=False, verbose_name='Banner'),
        ),
    ]
