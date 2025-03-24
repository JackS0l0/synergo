from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from main import views as mainviews
from django.conf.urls.i18n import i18n_patterns
handler404 = mainviews.custom_404
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',mainviews.index,name='home'),
    path('service/<str:slug>/',mainviews.ServiceDetail.as_view(),name='servicedetail'),
    path('blog/<str:slug>/',mainviews.BlogDetail.as_view(),name='blogdetail'),
    path('faq/',mainviews.faqPage,name='faqpage'),
    path('vacancies/',mainviews.vacancy,name='jobpage'),
    path('contact/',mainviews.contact,name='contactpage'),
    path('about/',mainviews.about,name='aboutpage'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", mainviews.set_language, name="set-language"),
]