from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'proekts'

urlpatterns = [
    path('', views.home, name='home'),
    path('add-proekt/', views.add_project, name="add_proekt"),
    path("apply/<int:project_id>/", views.apply_for_project, name="apply")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
