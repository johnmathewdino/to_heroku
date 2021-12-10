from django.contrib import admin
from .models import Evaluations, Evaluator, EvaluationGrade

admin.site.register(Evaluations)
admin.site.register(Evaluator)
admin.site.register(EvaluationGrade)
