from django.urls import path
from . import views
app_name = 'diagnosis'
urlpatterns = [
    path('upload/', views.upload_for_diagnosis, name='upload'),
    path('result/<int:pk>/', views.result_view, name='result'),
]
