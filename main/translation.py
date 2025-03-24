from django.contrib import admin
from modeltranslation.translator import TranslationOptions,register
from .models import Services,Projects,WhyWe,Vacancy,About,Blog,ContactInfo
@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ['desc']
@register(WhyWe)
class WhyWeTranslationOptions(TranslationOptions):
    fields = ['name','desc']
@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ['name','mini_desc','desc']
@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ['name','desc']
@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = ['name','desc']
@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ['name','desc']
@register(ContactInfo)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ['txt']