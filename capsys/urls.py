"""capsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('verification/', include('verify_email.urls')),
    path('',include('main.urls')),
    path('',include('register.urls')),
    path('',include('submissions.urls')),
    path('',include('forum.urls')),
    path('',include('guide.urls')),
    path('',include('proposalgroup.urls')),
    path('', include('proposaltitle.urls')),
    path('', include('proposalpanelists.urls')),
    path('',include('evaluation.urls')),
    path('',include('feedback.urls')),
    path('', include('plagiarism_checker.urls')),
    path('',include('manuscriptevaluations.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#FOR 404 AND 500 PAGE
handler404 = 'main.views.page404'
handler500 = 'main.views.page500'

# password_change/ [name='password_change']
# password_change/done/ [name='password_change_done']
# password_reset/ [name='password_reset']
# password_reset/done/ [name='password_reset_done']
# reset/<uidb64>/<token>/ [name='password_reset_confirm']
# reset/done/ [name='password_reset_complete']
