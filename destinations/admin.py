from django.contrib import admin
from .models import Destinations

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Destinations, PageAdmin)