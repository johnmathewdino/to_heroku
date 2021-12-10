from django.db import models
from django.contrib.auth.models import User
from proposaltitle.models import ProposeTitle
from register.models import UserProfile


class AdviserAndPanelist(models.Model):
    id =models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    adviser = models.ForeignKey(UserProfile, related_name="adviser", on_delete=models.CASCADE)
    title = models.ForeignKey(ProposeTitle, null=True, on_delete=models.CASCADE)
    panel1 = models.ForeignKey(UserProfile, related_name="panel1", on_delete=models.CASCADE)
    panel2 = models.ForeignKey(UserProfile, related_name="panel2", on_delete=models.CASCADE)
    panel3 = models.ForeignKey(UserProfile, related_name="panel3", on_delete=models.CASCADE)
    panel4 = models.ForeignKey(UserProfile, related_name="panel4", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
