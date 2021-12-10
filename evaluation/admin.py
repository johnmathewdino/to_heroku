from django.contrib import admin
from .models import Scheduler, SchedulerEvent, SchedulerDate

admin.site.register(Scheduler)
admin.site.register(SchedulerEvent)
admin.site.register(SchedulerDate)




