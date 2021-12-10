from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views, DeanViews, StudentViews, FacultyViews, CPViews

urlpatterns = [

    # FIRST GO HERE THEN GO TO VIEWS
    path('', views.directto, name="home"),

    # DEPARTMENT DEAN VIEWS
    path('dean/dashboard/', DeanViews.home, name="dean_home"),
    path('add_cp/', DeanViews.add_cp, name="add_cp"),
    path('add_faculty/', DeanViews.add_faculty, name="add_faculty"),
    path('add_student/', DeanViews.add_student, name="add_student"),
    path('dean/group/', DeanViews.add_group, name="group_list"),
    path('dean/edit_announcement/<int:id>', DeanViews.edit_announcement, name="edit_announcement"),
    path('dean/monitoring/',DeanViews.monitoring, name="monitoring"),

    # CP VIEWS
    path('cp/dashboard/', CPViews.home, name="cp_home"),
    

    # FACULTY VIEWS
    path('faculty/dashboard/', FacultyViews.home, name="faculty_home"),
    path('faculty/monitoring/', FacultyViews.facmonitoring, name="facmonitoring"),

    #STUDENT VIEWS
    path('student/dashboard/', StudentViews.home, name="student_home"),

    # TEST URLS#
    path('testlogin/', views.test, name='test'),
    
    # PAGE 404
    path('page404/', views.page404, name='page404'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

