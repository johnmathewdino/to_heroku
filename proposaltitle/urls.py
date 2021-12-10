from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from . import views

urlpatterns = [

    #Student View
    path("student/proposal/title/", views.StudentTitleview, name="Student_Title"),
    path("proposal/edit_title/<int:id>/", views.Edit_title, name="edit_title"),
    path("student/proposal/title/<int:id>/", views.StudentTitleCommentview, name="StudentTitleComment"),
    path('student/comment_reply/<int:id>/', views.Student_Comment_ReplyView, name="Student_Comment_ReplyView"),
    path('student/edit_reply/<int:id>/', views.Edit_comment_reply, name="Edit_comment_reply"),
    path('student/delete_reply/<int:id>/', views.delete_reply, name="delete_reply"),
    



    #Faculty View
    path("faculty/proposal/title/", views.FacultyTitleview, name="Faculty_Title"),
    path("proposal/titlelist/<int:id>/", views.TitleList, name="Title_List"),
    path("faculty/proposal/title/<int:id>/", views.FacultyTitleCommentView, name="FacultyTitleComment"),
    path("proposal/edit_comment/<int:id>/", views.Edit_comment, name="edit_comment"),
    path('cp/comment_reply/<int:id>/', views.Cp_ViewReply, name="Cp_ViewReply"),
    

    # path("proposal/delete/<int:id>/", views.delete_comment, name='Delete Commnet'),
    # path("proposal/list/<int:id>/", views.ProposeTitleResult, name="ProposeTitleResult"),
    # path("proposal/group_list/", views.ProposeTitleGroup, name="ProposeTitleGroupResult"),
    # path("proposal/edit_comment/<int:id>/", views.Edit_comment, name="edit_comment"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
