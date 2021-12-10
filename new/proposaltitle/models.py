from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ProposeTitle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=1000)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TitleComment(models.Model):
    author =models.ForeignKey(User, related_name='author', on_delete=models.CASCADE, null=True)
    title = models.ForeignKey(ProposeTitle, null=True, on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        comment = self.author.username + " - " + self.title.title
        return comment
