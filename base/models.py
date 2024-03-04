from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title
