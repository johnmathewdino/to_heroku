from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('feedback/student/', views.student_feedback, name="StudentFeedback"),
    path('feedback/faculty/', views.faculty_feedback, name="FacultyFeedback"),
    path('feedback/cp/', views.CP_feedback, name="CPFeedback"),
    path('feedback/reply/<int:id>/', views.CP_feedback_reply, name="FeedbackReply")


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
