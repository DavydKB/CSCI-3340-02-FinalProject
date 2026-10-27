from django.db import models
from django.conf import settings

# Create your models here.
class Post (models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name="posts"
    ) 
    title = models.CharField(max_length = 50)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
	    return self.title


class Profile (models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete = models.CASCADE
    )
    name = models.CharField(max_length = 50)
    bio = models.CharField(blank = True)

    def __str__(self):
	    return self.name


class Event (models.Model):
    name = models.CharField(max_length = 50)    
    description = models.TextField(blank = True)
    start_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
	    return self.name

class Club (models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(blank = True)

    def __str__(self):
	    return self.name