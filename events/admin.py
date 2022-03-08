from django.contrib import admin

# Register your models here.

from .models import Events, Tags


admin.site.register(Events)

admin.site.register(Tags)