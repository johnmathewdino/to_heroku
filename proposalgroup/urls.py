from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("student/proposal/group/", views.StudentGroupview, name="Group"),
    path("faculty/proposal/group/", views.FacultyGroupView, name="FacultyGroupView"),
    path("edit_group/<int:id>", views.Edit_group, name="Edit Group")


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
