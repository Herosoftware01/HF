from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.contrib.auth.models import User

class Complaint(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Unit = models.CharField(max_length=20,choices=[('Office','Office'),('Unit - 1','Unit - 1'),('Unit - 2','Unit - 2'),('Unit - 3','Unit - 3'),('Unit - 4','Unit - 4'),('Unit - 5','Unit - 5')])
    Complaint = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='complaints/', blank=True, null=True)
    AssignDept = models.CharField(max_length=20,choices=[('Electrician','Electrician'),('IT','IT')],default='Electrician')
    Priority = models.CharField(max_length=20,choices=[('⚪ Low','⚪ Low'),('🟡 Medium','🟡 Medium'),('🟠 Important','🟠 Important'),('🔴 Urgent','🔴 Urgent')],default='⚪ Low')
    Completed = models.BooleanField(default=False)
    EndTime = models.DateTimeField(null=True,blank=True)
    Rating = models.CharField(max_length=20,choices=[('⭐','⭐'),('⭐⭐','⭐⭐'),('⭐⭐⭐','⭐⭐⭐'),('⭐⭐⭐⭐','⭐⭐⭐⭐'),('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐')],default='⭐',null=True,blank=True)
    Feedback = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.Unit

    def user_can_complete(self, user):
        return User.objects.get(username='Service').exists()
    
    def admin_image_preview(self):
        if self.Image:
            return mark_safe(f'<img src="{self.Image.url}" alt="" width="100" style="border: 1px solid #100; border-radius:10%;"/>')
        return "No Image"
    admin_image_preview.short_description = "Image"

    def save(self, *args, **kwargs):
        if self.Completed:
            self.EndTime = timezone.localtime()
        super().save(*args, **kwargs)

