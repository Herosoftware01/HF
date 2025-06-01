from django.contrib import admin
from .models import Demo

class DemoAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
    list_filter = ('name', 'age')
    search_fields = ('name', 'age')
    ordering = ('name', 'age')

admin.site.register(Demo, DemoAdmin)