from .models import StudentFeedback
from django import forms

class StudentFeebackForm(forms.ModelForm):
    class Meta:
        model = StudentFeedback
        fields = ('feedback', 'feedback_reply',)
