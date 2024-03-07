from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default = None, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
