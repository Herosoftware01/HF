from django.contrib import admin
from .models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('Date', 'Unit', 'Complaint', 'admin_image_preview', 'AssignDept', 'Priority', 'Completed','EndTime','Rating','Feedback')
    list_filter = ('Completed','AssignDept','Priority')
    ordering = ('Date',)
    list_display_links = ('Date',)
    list_editable = ('Completed',)
    fieldsets = (
        (None, {
            'fields': ('Unit', 'Complaint', 'Image','AssignDept','Priority')
        }),
        ('Status', {
            'fields': ('Completed','EndTime')
        }),
        ('User Feedback', {
            'fields': ('Rating','Feedback')
        })
    )

admin.site.register(Complaint, ComplaintAdmin)