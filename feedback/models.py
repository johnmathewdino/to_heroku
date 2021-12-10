from django.db import models
from django.contrib.auth.models import User
from register.models import UserProfile


class StudentFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True, default="")
    feedback_reply = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
