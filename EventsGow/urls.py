"""EventsGow URL Configuration"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), #Authentication urls
    path('faq/', include('accounts.urls')), #Faq urls
    path('', include('events.urls'), name='events'), #Event urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
