from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

from django.utils.dateformat import format

# Create your models here.

class News(models.Model):
    author = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    audience = models.EnumField(default=1)
    disabled = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    # published = models.BooleanField(default=False, blank=True)
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False) for auto-updating func/button


class NewsContent(models.Model):
    news = models.ForeignKey(News, unique = True, on_delete=models.CASCADE)
    title = models.CharField (max_length=200)
    content = models.CharField (max_length=30000)
    image = models.CharField (max_length=200)
    locale = models.EnumField (default=1)
    timestamp = models.DateTimeField (auto_now=True, auto_now_add=True)

class NewsLanuage(models.Model):
    locale = models.EnumField(default=1)

    class Meta:
        ordering = ['-timestamp', '-updated']

    def __str__(self):
        return self.title

    def unix_time(self):
        return format(self.updated, 'U')

    

class LastUpdate(models.Model):
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def unix_time(self):
        return format(self.updated, 'U')

    def __str__(self):
        return self.unix_time()