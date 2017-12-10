# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Hot_News(models.Model):
    news_url = models.URLField()
    publish_time = models.DateTimeField () 
    repoter = models.CharField (max_length = 30) 
    headline = models.CharField (max_length = 70, unique = True)
    content = models.TextField()
    img_dir= models.CharField(max_length = 50)
    video_dir = models.CharField(max_length = 50)

    def __str__(self):
        return self.headline

    class Meta:
        db_table = 'Hot_News'
