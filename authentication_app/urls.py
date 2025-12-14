from django.urls import path

from . import views 

urlpatterns = [
    # urls for the log in and sign up logic
    path('register/', views.register_view, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]