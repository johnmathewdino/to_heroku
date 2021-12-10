from .models import ProposeTitle, TitleComment
from django import forms

class ProposeTitleForm(forms.ModelForm):
    class Meta:
        model = ProposeTitle
        fields =('title','description')


class TitleCommentForm(forms.ModelForm):
    class Meta:
        model = TitleComment
        fields = ('comment',)
