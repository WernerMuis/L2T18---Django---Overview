from django.db import models
from django.contrib.auth.models import User


# Class to allow the admin to add albums to the database.
class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


# Class to allow the admin to add live show details to the database.
class LiveShow(models.Model):
    date = models.DateField()
    venue = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.venue
