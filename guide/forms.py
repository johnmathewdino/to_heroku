from django import forms
from .models import guide, guide_topic



class GuideForm(forms.ModelForm):

    class Meta:
        model = guide
        fields = ['title','content','File']