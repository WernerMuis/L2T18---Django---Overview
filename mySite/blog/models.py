from django.db import models

# The Post class.
class Post(models.Model):
    """Model representing a post in the database.

    :param models.Model: The base class for all Django database models.
    :type models.Model: class
    :ivar title: The title of the post.
    :vartype title: CharField
    :ivar body: The body content of the post.
    :vartype body: TextField
    :ivar signature: The signature associated with the post, default is "Werner Miller".
    :vartype signature: CharField
    :ivar date: The date and time when the post was created.
    :vartype date: DateTimeField
    :return: A string representation of the post.
    :rtype: str
    """    
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default= "Werner Miller")
    date = models.DateTimeField()


    def __str__(self):
        return self.title
