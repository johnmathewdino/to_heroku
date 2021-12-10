from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views


urlpatterns = [
    path('topic/', views.topic, name="topic"),
    path('topic/forum/<int:id>/', views.forum, name="forum"),
    path('topic/forum/discussion/<int:id>/', views.discussion, name='forum_discussion'),

    path('topic/update/<int:id>/', views.update_topic, name="update_topic"),
    path('topic/delete_topic/<int:id>/', views.delete_topic, name="delete_topic"),

    path('topic/forum/<int:id>/edit/', views.update_forum, name="update_forum"),
    path('topic/delete_forum/<int:id>/', views.delete_forum, name="delete_forum"),

    path('topic/forum/discussion/<int:id>/edit/', views.update_reply, name='update_discussion'),
    path('topic/delete_reply/<int:id>/', views.delete_reply, name="delete_reply"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
