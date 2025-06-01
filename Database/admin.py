from django.contrib import admin
from .models import Demo

class DemoAdmin(admin.ModelAdmin):
    list_display = ('name', 'age','salary')
    list_filter = ('name', 'age','salary')
    search_fields = ('name', 'age','salary')
    ordering = ('name', 'age','salary')

admin.site.register(Demo, DemoAdmin)