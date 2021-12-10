from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from register.models import UserProfile

class SchedulerEvent(models.Model):
    scheduler_event = models.CharField(max_length=1000)

    def __str__(self):
        return self.scheduler_event

class SchedulerDate(models.Model):
    event_d = models.ForeignKey(SchedulerEvent, related_name="event_d", default="", null=True, on_delete=models.CASCADE)
    date_event = models.DateField(max_length=1000)

    def __str__(self):
        date = str(self.date_event)
        return date


class Scheduler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(SchedulerEvent, related_name="event", default="", blank=True, null=True, on_delete=models.CASCADE)
    date = models.ForeignKey(SchedulerDate, related_name="date", default="", blank=True, null=True,  on_delete=models.CASCADE)
    time = models.TimeField(blank=True)
    timestamp = models.DateTimeField(default=now)
    proponents = models.ForeignKey(UserProfile, related_name="proponents", on_delete=models.CASCADE, blank=True, null=True, default="")
    adv = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adv", null=True)

    def __str__(self):
        event = self.event.scheduler_event
        return event
