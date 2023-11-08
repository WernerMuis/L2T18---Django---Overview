from django.contrib import admin
from .models import Album, LiveShow

# Enabling the admin to add Albums and Live Show details to the database.
admin.site.register(Album)
admin.site.register(LiveShow)
