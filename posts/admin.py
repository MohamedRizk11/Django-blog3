from django.contrib import admin

# Register your models here.
from .models import post
class postadmin(admin.ModelAdmin):
    list_display=['title','publish_date']
    search_fields=['title','content']

admin.site.register(post,postadmin)