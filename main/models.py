from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db import models
class ContactMessage(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Ad Soyad")
    phone = models.PositiveBigIntegerField(verbose_name="Telefon Nömrəsi")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Göndərilmə tarixi")
    complated = models.BooleanField('Təhvil verildi',default=False)
    def __str__(self):
        return f"{self.full_name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    class Meta:
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'
class Services(models.Model):
    name=models.CharField('Xidmətin adı',max_length=200,default='none')
    desc=RichTextField('Məzmun',default='none')
    mini_desc=models.TextField('Kiçik məzmun',default='none')
    img=models.URLField('Şəkil',default='none')
    date=models.DateTimeField('Tarix',default=timezone.now)
    slug=models.SlugField('Slug',default='none')
    banner=models.BooleanField('Banner',default=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Servis'
        verbose_name_plural = 'Servislər'
class Projects(models.Model):
    name=models.CharField('Xidmətin adı',max_length=200,default='none')
    desc=RichTextField('Məzmun',default='none')
    img=models.URLField('Şəkil',default='none')
    date=models.DateTimeField('Tarix',default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Layhiə'
        verbose_name_plural = 'Layhiələr'
class WhyWe(models.Model):
    name=models.CharField('Xidmətin adı',max_length=200,default='none')
    desc=RichTextField('Məzmun',default='none')
    img=models.URLField('Şəkil',default='none')
    date=models.DateTimeField('Tarix',default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Xüsusiyyət'
        verbose_name_plural = 'Xüsusiyyətlər'
class Resume(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cv_file = models.FileField(upload_to='cv_files/')
    date=models.DateTimeField('Tarix',default=timezone.now)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CV-lər'
class Vacancy(models.Model):
    name=models.CharField('Vakansiyanın adı',max_length=200,default='none')
    desc=RichTextField('Məzmun',default='none')
    date=models.DateTimeField('Tarix',default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Vakansiya'
        verbose_name_plural = 'Vakansiyalar'
class About(models.Model):
    desc=RichTextField('Məzmun',default='none')
    def __str__(self):
        return f'Haqqımızda'
    class Meta:
        verbose_name = 'Haqqımızda'
        verbose_name_plural = 'Haqqımızda'