from django.urls import path
from . import views  

urlpatterns = [
   
    path('dashboard/', views.upload_view, name='dashboard'),
     path('upload/', views.upload_view, name='upload_file'),
]