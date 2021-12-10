from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('submissions/', views.SubmissionTitleViews, name = "submissions"),
    path('submissions/<int:id>/', views.StudentSubmitViews, name="submit"),
    path('submissions-form/<int:Titleid>/',  views.StudentSubmitViewsForm, name="submission-form"),
    path('submissions-form/<int:id>/edit/', views.EditStudentSubmitViewsForm, name="edit-submission-form"),

    path('cp/submissions/<int:id>/', views.CPSubmissionsView, name="cp_submissions"),
    path('cp/submissionscomment/<int:id>/', views.CPSubmissionComment, name='Submissions Comment'),
    path('cp/edit_submission/<int:id>/', views.Edit_SubmissionTitleViews, name="Edit_SubmissionTitleViews"),
    path('cp/delete_submission/<int:id>/', views.Delete_SubmissionTitleViews, name="Delete_SubmissionTitleViews"),

    path('faculty/submissions/<int:id>', views.FacultySubmissionsView, name="faculty_submissions"),

    path('student/submissionscomment/<int:id>/', views.StudentCommentView, name='Student Comment View'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
