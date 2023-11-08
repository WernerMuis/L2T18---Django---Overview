from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('show_user/', views.show_user, name='show_user'),
    path('registration/', views.registration, name='registration'),
]