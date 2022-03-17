from django.contrib import admin

# Register your models here.
from .models import CustomUser
from django.contrib.sites.models import Site



admin.site.register(CustomUser)
# admin.site.register(Site)