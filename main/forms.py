from django import forms
from .models import Announcement, UserBatchUpload

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('detail',)

