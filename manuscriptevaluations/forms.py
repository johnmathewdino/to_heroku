from django.db.models import fields
from .models import Evaluations
from django import forms

class EvaluationsForm(forms.ModelForm):
    class Meta:
        model = Evaluations
        fields = ('recommendations', 'page' )

