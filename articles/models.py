from email.policy import default
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# title author text
options = (("published", "Published"), ("draft", "Draft"))


class ArticleObjects(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    description = models.TextField(default="Description not available")
    text = models.TextField()
    status = models.CharField(max_length=20, choices=options, default="published")
    slug = models.SlugField(max_length=100, unique=True, unique_for_date="date_created")
    upload_pics = models.ImageField(
        default="default.jpg", upload_to="article_pics", null=True
    )
    objects = models.Manager()
    postObject = ArticleObjects()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"
