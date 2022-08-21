from django.db import models

# Create your models here.
class Images(models.Model):
    content = models.ImageField(width_field=100,height_field=300,verbose_name="Upload image here",upload_to='images')
    date = models.DateTimeField(auto_now=True)