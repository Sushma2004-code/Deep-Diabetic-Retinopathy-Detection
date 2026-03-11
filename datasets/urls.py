from django.urls import path
from . import views
app_name = 'datasets'
urlpatterns = [
    path('', views.dataset_list, name='list'),
    path('upload/', views.upload_image, name='upload'),
    path('export/csv/', views.export_csv, name='export_csv'),
]
