from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Topic (models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=now)


    def __str__(self):
        return self.title

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    post_id = models.AutoField
    title = models.CharField(max_length=1000, default="")
    post_content = models.TextField()
    timestamp = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="forum/%Y-%m-%d", blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment_content = models.TextField()
    timestamp = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images/forum/", default="", blank=True, null=True)

    def __str__(self):
        comment_title = str(self.topic) + str(self.post)
        return comment_title

