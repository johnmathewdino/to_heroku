from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

from register import views
from django.contrib.auth import views as auth_views #import this


urlpatterns = [
    path('register/', views.register, name= "register"),
    # path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_reset/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_reset/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset/password_reset.html'), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset/password_reset_form.html'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset/password_reset_complete.html'), name='password_reset_complete'),
    path("profile/", views.profile, name="profile"),
    path('activate/<uidb64>/<token>/',views.activate, name='activate')

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
