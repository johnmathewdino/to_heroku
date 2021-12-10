from django.forms import fields
from .models import ProposeTitle, TitleComment, CommentReply
from django import forms

class ProposeTitleForm(forms.ModelForm):
    class Meta:
        model = ProposeTitle
        fields =('title','description')



class TitleCommentForm(forms.ModelForm):
    class Meta:
        model = TitleComment
        fields = ('comment',)


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ('reply',)