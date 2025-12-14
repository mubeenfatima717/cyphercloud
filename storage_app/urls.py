from django.urls import path
from . import views  

urlpatterns = [
   
    path('dashboard/', views.upload_view, name='dashboard'),
     path('upload/', views.upload_view, name='upload_file'),
     path('download/<int:file_id>/', views.download_file, name='download_file'),
     path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
     path('create_folder/', views.create_folder, name='create_folder'),
    path('dashboard/<int:folder_id>/', views.upload_view, name='dashboard_folder'),
    
]