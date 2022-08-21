from django.db import models

# Create your models here.
class Images(models.Model):
    content = models.ImageField(verbose_name="Upload image here",upload_to='images')
    date = models.DateTimeField(auto_now=True)