from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('evaluation/scheduler/', views.CP_SchedulerView, name='Scheduler'),
    path('evaluation/schedule/', views.Faculty_SchedulerView, name="Schedule"),
    path('evaluation/student_sched/', views.Student_SchedulerView, name='Student Schedule'),
    path('evaluation/faculty_add_sched/<int:id>/', views.Faculty_SchedulerView_Add, name='FacultyAddSched'),

    path('evaluation/edit_scheduler/<int:id>/', views.Edit_CPScheduler, name="Edit_CPScheduler"),
    path('evaluation/delete_scheduler/<int:id>/', views.Delete_CPScheduler, name="Delete_CPScheduler"),
    path('evaluation/edit_date/<int:id>/', views.Edit_CPdate, name="Edit_CPdate"),
    path('evaluation/delete-date/<int:id>/', views.Delete_SchedDate, name='Delete_SchedDate'),

    path('evaluation/edit_scheduler_add/<int:id>/', views.Edit_faculty_scheduler, name="Edit_faculty_scheduler"),
    path('evaluation/delete_scheduler_add/<int:id>/', views.Delete_Faculty_Scheduler, name="Delete_Faculty_Scheduler"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
