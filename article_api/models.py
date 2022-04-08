from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

options = (("draft", "Draft"), ("published", "Published"))
# Create your models here.
class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    text = models.TextField()
    status = models.CharField(max_length=10, choices=options, default="published")
    slug = models.SlugField(max_length=100, unique=True, null=False)
    objects = models.Manager()
    postObject = PostObjects()

    def __str__(self):
        return self.title


class AuthorProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    about = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return f"{self.username.username}"

    ordering = [username, about]
