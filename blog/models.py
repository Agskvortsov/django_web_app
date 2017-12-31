from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
#    image = models.ImageField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
	

	
#from __future__ import unicode_literals
#from django.db import models
#from django.contrib.auth.models import (
#    BaseUserManager, AbstractBaseUser
#)
#
## Create your models here.
#class Photo(models.Model):
#    img = models.Manager()
#    title = models.CharField(max_length=200)
#    width = models.IntegerField(default=0)
#    height = models.IntegerField(default=0)
#    image = models.ImageField()
#    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#    def __unicode__(self):
#        return self.title
