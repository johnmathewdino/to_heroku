from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('guide/',views.Guide, name="guide"),
    path('guide/<int:id>/', views.guidepost, name="guidepost"),

    path('guide/edit/<int:id>/', views.Edit_Guide, name="Edit_Guide"),
    path('guide/delete<int:id>/', views.Delete_guide, name='Delete_guide'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
