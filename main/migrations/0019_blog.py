# Generated by Django 5.1.7 on 2025-03-22 21:41

import ckeditor.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_about_desc_az_about_desc_en_about_desc_ru'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=200, verbose_name='Xidmətin adı')),
                ('name_az', models.CharField(default='none', max_length=200, null=True, verbose_name='Xidmətin adı')),
                ('name_en', models.CharField(default='none', max_length=200, null=True, verbose_name='Xidmətin adı')),
                ('name_ru', models.CharField(default='none', max_length=200, null=True, verbose_name='Xidmətin adı')),
                ('desc', ckeditor.fields.RichTextField(default='none', verbose_name='Məzmun')),
                ('desc_az', ckeditor.fields.RichTextField(default='none', null=True, verbose_name='Məzmun')),
                ('desc_en', ckeditor.fields.RichTextField(default='none', null=True, verbose_name='Məzmun')),
                ('desc_ru', ckeditor.fields.RichTextField(default='none', null=True, verbose_name='Məzmun')),
                ('img', models.URLField(default='none', verbose_name='Şəkil')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Tarix')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
