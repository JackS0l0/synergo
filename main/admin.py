from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import ContactMessage,Services,Projects,WhyWe,Resume,Vacancy
from import_export.admin import ExportMixin
from import_export import resources
@admin.register(Resume)
class ResumeControl(admin.ModelAdmin):
    list_display=['full_name','date']
    def has_change_permission(self, request, obj=None):
        return False
class ContactMessageResource(resources.ModelResource):
    class Meta:
        model = ContactMessage
@admin.register(WhyWe)
class WhyWeControl(TranslationAdmin):
    group_fieldsets = True  
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
@admin.register(Projects)
class ProjectsControl(TranslationAdmin):
    group_fieldsets = True  
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
@admin.register(Services)
class ServicesControl(TranslationAdmin):
    list_display=['name','banner']
    list_filter=['banner']
    group_fieldsets = True  
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
@admin.register(ContactMessage)
class ContactMessageControl(ExportMixin, admin.ModelAdmin):
    resource_class = ContactMessageResource
    list_display = ['full_name','created_at','complated']
    readonly_fields = ["full_name", "phone", "email", "message", "created_at"]
    search_fields = ['full_name']
    list_filter=['created_at','complated']
    def has_change_permission(self, request, obj=None):
        return True  # Redaktəyə icazə veririk
    def has_add_permission(self, request):
        return False  # Yeni mesaj əlavə edilə bilməz
    def has_delete_permission(self, request, obj=None):
        return True  # Silməyə icazə veririk
@admin.register(Vacancy)
class VacancyControl(TranslationAdmin):
    list_display=['name','date']
    search_fields=['name']
    group_fieldsets = True  
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }