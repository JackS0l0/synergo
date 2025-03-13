# Generated by Django 5.1.7 on 2025-03-11 05:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomePack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=200, verbose_name='Başlıq')),
                ('name_az', models.CharField(default='none', max_length=200, null=True, verbose_name='Başlıq')),
                ('name_en', models.CharField(default='none', max_length=200, null=True, verbose_name='Başlıq')),
                ('name_ru', models.CharField(default='none', max_length=200, null=True, verbose_name='Başlıq')),
                ('text', ckeditor.fields.RichTextField(default='none', verbose_name='Məzmun')),
                ('text_az', ckeditor.fields.RichTextField(default='none', null=True, verbose_name='Məzmun')),
                ('text_en', ckeditor.fields.RichTextField(default='none', null=True, verbose_name='Məzmun')),
                ('text_ru', ckeditor.fields.RichTextField(default='none', null=True, verbose_name='Məzmun')),
                ('img', models.URLField(default='none', verbose_name='Şəkil')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Bannerlər',
            },
        ),
    ]
