from django.db import models
from django.contrib.auth.models import User


# Class to allow the admin to add albums to the database.
class Album(models.Model):
    """Model representing an album in the database.

    :param models.Model: The base class for all Django database models.
    :type models.Model: class
    :ivar title: The title of the album.
    :vartype title: str
    :ivar release_date: The release date of the album.
    :vartype release_date: DateField
    :ivar description: A description of the album.
    :vartype description: TextField
    :return: A string representation of the album.
    :rtype: str
    """    
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


# Class to allow the admin to add live show details to the database.
class LiveShow(models.Model):
    """Model representing live show details in the database.

    :param models.Model: The base class for all Django database models.
    :type models.Model: class
    :ivar date: The date of the live show.
    :vartype date: DateField
    :ivar venue: The venue where the live show takes place.
    :vartype venue: CharField
    :ivar location: The location of the live show.
    :vartype location: CharField
    :return: A string representation of the live show.
    :rtype: str
    """    
    date = models.DateField()
    venue = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.venue
