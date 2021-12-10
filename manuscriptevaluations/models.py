# from os import O_TMPFILE
from django.db import models
from django.contrib.auth.models import User
from submissions.models import StudentSubmit, SubmissionTitle

class Evaluator(models.Model):
    eval_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    submission_user = models.ForeignKey(StudentSubmit, null=True, on_delete=models.CASCADE)

    def __str__(self):
        evaluation = self.eval_user.username
        return evaluation

class Evaluations(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    submission = models.ForeignKey(StudentSubmit, null=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=250, null=True, blank=True, default="")
    recommendations = models.TextField(max_length=1000, null=True, blank=True, default="")
    page = models.CharField(max_length=100, null=True, blank=True, default="")

    def __str__(self):
        contents = self.user.username
        return contents

class EvaluationGrade(models.Model):
    evaluator = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    student_submission = models.ForeignKey(StudentSubmit, null=True, default="", on_delete=models.SET_NULL)
    PF = models.CharField(max_length=100, null=True, default="", blank=True)
    N = models.FloatField(null=True, default="", blank=True)

    def __str__(self):
        return str(self.evaluator)+ " - " + str(self.student_submission)



