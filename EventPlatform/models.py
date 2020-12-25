from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(blank=True)
    author = models.CharField(max_length=150)
    description = models.TextField()
    picture = models.ImageField(upload_to='images')