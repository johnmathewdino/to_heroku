from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case


# Create your models here.

class ProposeTitle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    group = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1000, null=True, default="", blank=True)
    edited = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.title



class TitleComment(models.Model):
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    title = models.ForeignKey(ProposeTitle, null=True, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        comment = self.author.username + " - " + self.title.title
        return comment

class CommentReply(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, default="")
    cp_comment = models.ForeignKey(TitleComment, null=True, on_delete=CASCADE)
    reply = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
