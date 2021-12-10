from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('cp/evaluations/', views.CPEvaluationView, name='CPEvaluations'),
    path('cp/evaluatesubmissions/<int:id>/', views.CPEvaluateSubmissions, name='Evaluate Submissions'),
    path('cp/evaluate/<int:id>/', views.CPEvaluate, name='CP Evaluate'),

    path('student/evaluation', views.StudentEvaluationView, name='Student Evaluation'),
    path('student/evaluatedstudent/<int:id>/', views.StudentEvaluate, name='Evaluated Student'),

    path('faculty/evaluation/', views.FacultyevaluationView, name='FacultyEvaluationView'),
    path('faculty/evaluatesubmissions/<int:id>/', views.FacultyEvaluateSubmissions, name='FacultyEvaluateSubmissions'),
    path('faculty/evaluate/<int:id>/', views.FacultyEvaluate, name='Faculty Evaluate'),
    path('faculty/edit_evaluate/<int:id>/', views.Edit_FacultyEvaluate, name='Edit_FacultyEvaluate'),
    path('faculty/delelte_evaluate/<int:id>/', views.Delete_FacultyEvaluate, name="Delete_FacultyEvaluate"),
    path('faculty/edit_evaluation_grade/<int:id>/', views.Edit_EvaluationGrade, name="Edit_Evaluation_Grade"),
    path('faculty/delete_evaluation_grade<int:id>/', views.Delete_EvaluationGrade, name="Delete_EvaluationGrade")



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
