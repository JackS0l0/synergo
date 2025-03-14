from django import forms
from .models import ContactMessage,Resume
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["full_name", "phone", "email", "message"]
class CVForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['full_name', 'email', 'phone', 'cv_file']