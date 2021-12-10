import os
from typing import Set

from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields import DateField
from django.utils.timezone import now
from .validators import validate_file_extension
# Create your models here.

class SubmissionTitle(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    submission_detail = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    duedate = models.DateTimeField()
    status = models.IntegerField(default=0)
    for_evaluation = models.BooleanField(default=False, null=True)
    type_of_eval_grade = models.CharField(max_length=50, null=True, default="")


    def __str__(self):
        return self.title



class StudentSubmit(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    submission_title = models.ForeignKey(SubmissionTitle, null=True, on_delete=models.CASCADE)
    submit_content = models.TextField(null=True,blank=True)
    pdf_submit = models.FileField(upload_to='submissions/%Y-%m-%d/', null=True, blank=True, max_length=500, validators=[validate_file_extension])
    filename = models.CharField(max_length=1000, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(default="no submission", max_length=100)
    for_eval_submit = models.BooleanField(default=False, null=True)
    eval_grade_submit = models.CharField(max_length=100, null=True)
    sub_evaluator = models.IntegerField(null=True, default=0)
    if_seen = models.IntegerField(null=True, default=0)


    def __str__(self):
        comment_title = self.user.username + " - " + self.submission_title.title
        return comment_title

class CommentSubmit(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    submission_content = models.ForeignKey(StudentSubmit, null=True, default="", on_delete=models.SET_NULL)
    comment_content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_content


# class Rubrix(models.Model):
#     submission_title = models.ForeignKey(SubmissionTitle, null=True, on_delete=models.CASCADE)
#     rub_title = models.CharField(max_length=100)
#     rub_description = models.CharField(max_length=250)
#     evaluator = models.ForeignKey(User, on_delete=SET_NULL, null=True)
#     student_submission = models.ForeignKey(StudentSubmit, on_delete=SET_NULL, null=True)
#     grade = models.FloatField(null=True)

#     def __str__(self):
#          return self.rub_title + " " + str(self.submission_title)
