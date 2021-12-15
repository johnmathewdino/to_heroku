from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class guide_topic(models.Model):
    guidetopic = models.CharField(max_length=1000)
    def __str__(self):
        return self.guidetopic

class guide(models.Model):
    topic = models.ForeignKey(guide_topic, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=1000)
    content = models.TextField()
    File = models.FileField(upload_to='guide/%Y-%m-%d', null=True, blank=True)
    image = models.ImageField(upload_to="guide/",null=True, blank=True)

    def __str__(self):
        return self.title



