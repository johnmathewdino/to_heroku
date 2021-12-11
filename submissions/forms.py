from django import forms
from .models import SubmissionTitle, StudentSubmit, CommentSubmit
from django import forms

class SubmissionsForm(forms.ModelForm):
    class Meta:
        model = SubmissionTitle
        fields = ('title','submission_detail','duedate')


class SubmitForm(forms.ModelForm):
    class Meta:
        model = StudentSubmit
        fields = ('submit_content', 'pdf_submit')

    def __init__(self, *args, **kwargs):
        super(SubmitForm, self).__init__(*args, **kwargs)
        self.fields['pdf_submit'].widget.attrs.update({
            'accept': '.pdf'
        })

    def __init__(self, *args, **kwargs):
        super(SubmitForm, self).__init__(*args, **kwargs)
        self.fields['submit_content'].label = ""
        self.fields['pdf_submit'].label = ""


class CommentSubmitForm(forms.ModelForm):
    class Meta:
        model = CommentSubmit
        fields = ('comment_content',)



