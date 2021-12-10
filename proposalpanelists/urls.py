from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("student/proposal/adviserandpanelist/", views.StudentAdviserAndPanelistView, name="StudentAdviserAndPanelistView"),
    path("faculty/proposal/adviserandpanelist/", views.FacultyAdviserAndPanelistView, name="FacultyAdviserAndPanelistView"),

#     path('student/proposal/edit_adpa/<int:id>/', views.Edit_StudentAdviserAndPanelistView, name='Edit_StudentAdviserAndPanelistView'),
    path("proposal/delete_aap/<myid>/", views.delete_adviserandpanelist, name="deleted"),


    path("faculty/proposal/requests/", views.faculty_student_request, name="faculty_student_request"),
    path("faculty/proposal/requests/adviser/<int:id>/", views.faculty_student_request_adviser, name="faculty_student_request_adviser"),
    path("faculty/proposal/requests/panel1/<int:id>/", views.faculty_student_request_panel1, name="faculty_student_request_panel1"),
    path("faculty/proposal/requests/panel2/<int:id>/", views.faculty_student_request_panel2, name="faculty_student_request_panel2"),
    path("faculty/proposal/requests/panel3/<int:id>/", views.faculty_student_request_panel3, name="faculty_student_request_panel3"),
    path("faculty/proposal/advisoreegrouprequests/<int:id>/", views.AdviserViewRequestsOfAdvisoree, name="AdviserViewRequestsOfAdvisoree"),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

