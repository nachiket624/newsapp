import datetime
from django.db import models
from django.utils.timezone import now
from embed_video.fields import EmbedVideoField

# Create your models here.
class Item(models.Model):
    video = EmbedVideoField()
    


class category(models.Model):
    category = models.CharField(max_length=60,unique=True)

    def __str__(self):
        return  self.category
class news(models.Model):
    headding  = models.TextField(max_length=600,blank=True)
    location = models.CharField(max_length=100,blank=True)
    para1  = models.TextField(max_length=1200,blank=True)
    para2  = models.TextField(max_length=1200,blank=True)
    tag = models.CharField(max_length=600,blank=True)
    img = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.CharField(max_length=350,blank=False)
    category = models.ForeignKey(category,max_length=100,blank=True,on_delete=models.CASCADE)
    youtube = models.CharField(max_length = 900,blank=True)

    def __str__(self):
        return self.headding
    

class socialmedia(models.Model):
    whatapp = models.URLField(max_length = 900,blank=True)
    youtube = models.URLField(max_length = 900,blank=True)
    twitter = models.URLField(max_length = 900,blank=True)
    facebook = models.URLField(max_length = 900,blank=True)

class herosection(models.Model):
    headding  = models.TextField(max_length=600,blank=True)
    location = models.CharField(max_length=100,blank=True)
    para1  = models.TextField(max_length=1200,blank=True)
    para2  = models.TextField(max_length=1200,blank=True)
    tag = models.CharField(max_length=600,blank=True)
    img = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.CharField(max_length=350,blank=False)
    category = models.ForeignKey(category,max_length=100,blank=True,on_delete=models.CASCADE)
    youtube = models.CharField(max_length = 900,blank=True)
    
    def __str__(self):
        return self.headding

