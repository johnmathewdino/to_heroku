from django.db.models import fields
from .models import Scheduler
from django import forms

class CP_SchedulerViewForm(forms.ModelForm):
    disabled_fields = ('timestamp',)
    class Meta:
        model = Scheduler
        fields = ('timestamp',)

    def __init__(self, *args, **kwargs):
        super(CP_SchedulerViewForm, self).__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True

    
