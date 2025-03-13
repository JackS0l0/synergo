# Generated by Django 5.1.7 on 2025-03-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_welcomepack_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='Ad Soyad')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefon Nömrəsi')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Mesaj')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Göndərilmə tarixi')),
            ],
            options={
                'verbose_name': 'Mesaj',
                'verbose_name_plural': 'Mesajlar',
            },
        ),
    ]
