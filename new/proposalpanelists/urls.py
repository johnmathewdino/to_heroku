from django.urls import path
from . import views

urlpatterns = [
    path("proposal/adviserandpanelist/", views.AdviserAndPanelistView, name="AdviserAndPanelist"),
    path("proposal/delete_aap/<myid>/", views.delete_adviserandpanelist, name="deleted"),


]
