# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import markdown
from django.utils.html import strip_tags
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags=models.ManyToManyField(Tag,blank=True)
    views=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('myplace:detail', kwargs={'pk': self.pk})
    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])

    def save(self,*args,**kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=['markdown.extensions.extra','markdown.extensions.codehilite',])
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Post,self).save(*args,**kwargs)
