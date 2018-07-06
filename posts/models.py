from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

from django.utils.dateformat import format

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    #published = models.BooleanField(default=False, blank=True)
    title = models.CharField(max_length=200)
    audience = models.EnumField(default=1)
    image = models.CharField(max_length=200)
    content = models.CharField(max_length=30000)
    disabled = models.BooleanField(default=False)
    #updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
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