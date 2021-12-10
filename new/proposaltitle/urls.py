from django.urls import path
from . import views

urlpatterns = [
    path("proposal/title/", views.Titleview, name="Title"),
    path("proposal/titlelist/<int:id>/", views.TitleList, name="Title List"),
    path("proposal/title/<int:id>/", views.TitleCommentview, name="TitleComment"),
    path("proposal/delete/<int:id>/", views.delete_comment, name='Delete Commnet'),
    path("proposal/list/<int:id>/", views.ProposeTitleResult, name="ProposeTitleResult"),
    path("proposal/group_list/", views.ProposeTitleGroup, name="ProposeTitleGroupResult"),
    path("proposal/edit_title/<int:id>/", views.Edit_title, name="edit_title"),
    path("proposal/edit_comment/<int:id>/", views.Edit_comment, name="edit_comment")

]
