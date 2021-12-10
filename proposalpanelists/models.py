from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from proposaltitle.models import ProposeTitle
from register.models import UserProfile


class AdviserAndPanelist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    adviser = models.ForeignKey(UserProfile, related_name="adviser", on_delete=models.CASCADE)
    proposed_title = models.ForeignKey(ProposeTitle, null=True, on_delete=models.CASCADE)
    final_title = models.CharField(blank=True, default="", max_length=1000)
    panel1 = models.ForeignKey(UserProfile, related_name="selectpanel1", on_delete=models.CASCADE, null=True)
    panel2 = models.ForeignKey(UserProfile, related_name="selectpanel2", on_delete=models.CASCADE, null=True)
    panel3 = models.ForeignKey(UserProfile, related_name="selectpanel3", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + "Adviser and Panelists"

class Adviserrequest(models.Model):
    user = models.ForeignKey(User,  null=True, on_delete=models.CASCADE)
    name = models.ForeignKey(User, related_name="advisername", null=True, on_delete=models.CASCADE)
    proposedtitle = models.CharField(max_length=254, blank=False, null=False, default=None)
    finaltitle = models.CharField(max_length=254, blank=False, null=False, default=None)
    titledescription = models.TextField(default=None, null=True,)
    status = models.CharField(default='pending', max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(default=now, null=True,)

    def __str__(self):
        return str(self.user) + " requests for " + str(self.name)

class Panel1request(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.ForeignKey(User, related_name="panel1name", null=True, on_delete=models.CASCADE)
    status = models.CharField(default='pending', max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(default=now, null=True,)

    def __str__(self):
        return str(self.user) + " requests for " + str(self.name)


class Panel2request(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.ForeignKey(User, related_name="panel2name", null=True, on_delete=models.CASCADE)
    status = models.CharField(default='pending', max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(default=now, null=True)

    def __str__(self):
        return str(self.user) + " requests for " + str(self.name)


class Panel3request(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.ForeignKey(User, related_name="panel3name", null=True, on_delete=models.CASCADE)
    status = models.CharField(default='pending', max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(default=now, null=True,)

    def __str__(self):
        return str(self.user) + " requests for " + str(self.name)

class Limitation(models.Model):
    limit = models.IntegerField(default=10)

    def __str__(self):
        return str(self.limit)
