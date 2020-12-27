from django.db import models



class Event(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(blank=True)
    author = models.CharField(max_length=150)
    description = models.TextField()
    picture = models.ImageField(upload_to='images', blank=True)
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, unique=True, db_index=True)


   