from django.contrib import admin
from django.db import models

#Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=60)
    body=models.TextField()
    created=models.DateField(auto_now=True)
    updated=models.DateField(auto_now=True)
    def __unicode__(self):
        return self.title+" "+self.body
class Comment(models.Model):
    body=models.TextField()
    author=models.CharField(max_length=60)
    created=models.DateField(auto_now=True)
    updated=models.DateField(auto_now=True)
    post=models.ForeignKey(Post, related_name='comments')
    def __unicode__(self):
        return self.author

class PostAdmin(admin.ModelAdmin):
    list_display=('title','created','updated')
    search_fields=('title','body')
    list_filter=('created',)
    inline=['CommentInline']

class CommentAdmin(admin.ModelAdmin):
    def first_sixty_xters(self):
        return self.body[:60]
    list_display=('post','author','first_sixty_xters','created','updated')
    list_filter=('created',)


class CommentInline(admin.TabularInline):
    pass

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)




