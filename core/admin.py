from django.contrib import admin
from core.models import Images
# Register your models here.
@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'content','date']
    
