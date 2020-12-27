from django.db import models
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(blank=True)
    author = models.CharField(max_length=150)
    description = models.TextField()
    picture = models.ImageField(upload_to='images', blank=True)
    location = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title





   