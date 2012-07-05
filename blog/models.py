from django.contrib import admin
from django.db import models

#Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=60)
    body=models.TextField()
    created=models.DateField(auto_now=True)
    updated=models.DateField(auto_now=True)
    def __unicode__(self):
        return self.title,self.body,self.created
class Comment(models.Model):
    body=models.TextField()
    author=models.CharField(max_length=60)
    created=models.DateField(auto_now=True)
    post=models.ForeignKey(Post)
    def __unicode__(self):
        return self.post,self.author
admin.site.register(Post)
admin.site.register(Comment)

