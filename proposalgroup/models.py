from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now



class Group(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="currentUser", null=True)
    groupname = models.CharField(max_length=225, default="")
    mem1 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="mem1", null=True, )
    mem2 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="mem2", null=True, )
    mem3 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="mem3", null=True, )
    mem4 = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="mem4", null=True, )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.groupname