from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('albums/', views.album_page, name='album_page'),
    path('live-shows/', views.live_shows_page, name='live_shows_page'),
]
