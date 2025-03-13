from django.shortcuts import render,redirect
from .forms import ContactForm
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve,reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from .models import Services,Projects
from django.views.generic import DetailView
from django.contrib import messages
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
def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
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