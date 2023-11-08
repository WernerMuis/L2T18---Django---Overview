from django.db import models

# The Post class.
class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default= "Werner Miller")
    date = models.DateTimeField()


    def __str__(self):
        return self.title
