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
    date_updated = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_posts",
        blank=True
    )

    def __str__(self):
	    return self.title

class PostMedia(models.Model):
    MEDIA_TYPES = [
        ("image", "Image"),
        ("video", "Video"),
    ]    

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="media"
    )

    file = models.FileField(upload_to="post_media/")
    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPES
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.media_type} for {self.post}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    likes = models.ManyToManyField(
    settings.AUTH_USER_MODEL,
    related_name="liked_comments",
    blank=True
    )
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date_created"]
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class Profile (models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete = models.CASCADE
    )
    name = models.CharField(max_length = 50)
    bio = models.TextField(blank = True)

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