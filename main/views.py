import os
import requests
from .forms import ContactForm
from django.conf import settings
from urllib.parse import urlparse
from django.contrib import messages
from django.utils import translation
from .models import Services,Projects
from django.views.generic import DetailView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls.base import resolve,reverse
from django.urls.exceptions import Resolver404
from dotenv import load_dotenv
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "Sənin_Chat_ID"
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Mesaj uğurla göndərildi!")
    else:
        print(f"Telegram API xəta baş verdi: {response.status_code}")
        print(f"Cavab məzmunu: {response.text}")
def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get("full_name", "Naməlum")
            # phone
            phone = form.cleaned_data.get("phone", "Naməlum")
            email = form.cleaned_data.get("email", "Naməlum")
            message_text = form.cleaned_data.get("message", "")
            telegram_message = f"📩 Yeni Mesaj!\n\n👤 Ad: {full_name}\n📧 Email: {email}\n📱 Telefon: {phone}\n💬 Mesaj: {message_text}"
            send_telegram_message(telegram_message)
            messages.success(request, "Mesajınız uğurla göndərildi!")
            return redirect('/')
    else:
        form = ContactForm()
    data={
        'title':'Synerge',
        'form':form,
        'servicesInBanner':Services.objects.all().order_by('-date'),
        'services':Services.objects.all().order_by('-date')[0:6],
        'projects':Projects.objects.all().order_by('-date')[0:8],
    }
    return render(request, 'index.html', data)
class ServiceDetail(DetailView):
    model = Services
    template_name = 'post.html'
    context_object_name = 'service'
    def get_context_data(self, **kwargs):
        data=super(ServiceDetail,self).get_context_data(**kwargs)
        data['services']=Services.objects.all().order_by('-date')
        data['title']=self.object.name
        return data
def faqPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get("full_name", "Naməlum")
            phone = form.cleaned_data.get("phone", "Naməlum")
            email = form.cleaned_data.get("email", "Naməlum")
            message_text = form.cleaned_data.get("message", "")
            telegram_message = f"📩 Yeni Mesaj!\n\n👤 Ad: {full_name}\n📧 Email: {email}\n📱 Telefon: +{phone}\n💬 Mesaj: {message_text}"
            send_telegram_message(telegram_message)
            messages.success(request, "Mesajınız uğurla göndərildi!")
            return redirect('/')
    else:
        form = ContactForm()
    data={
        'title':'Synergo - FAQ',
        'form':form,
        'services':Services.objects.all().order_by('-date'),
    }
    return render(request, 'faq.html', data)
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
def vacancy(request):
    data={
        'title':'Synergo - Vacancies',
        'services':Services.objects.all().order_by('-date'),
    }
    return render(request,'job.html',data)