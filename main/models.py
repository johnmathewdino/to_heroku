from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
User = settings.AUTH_USER_MODEL



# Create your models here.

class Announcement(models.Model):
    detail = models.TextField()
    timestamp = models.DateTimeField(default=now)


    def __str__(self):
        title = str(self.timestamp.date()) + " - "+ self.detail
        return title

class Code(models.Model):
    choices = (
        ("Student", "Student"),
        ("Faculty", "Faculty")
    )
    code = models.CharField(max_length=6, blank=False, null=False, unique=True)
    role = models.CharField(max_length=20, choices=choices)

    def __str__(self):
        return self.role


class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.SET_NULL, null=True)
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username


class UserBatchUpload(models.Model):
    name = models.FileField(upload_to='batchupload/%Y-%m-%d', null=True, blank=True)

    def __str__(self):
        return self.name

