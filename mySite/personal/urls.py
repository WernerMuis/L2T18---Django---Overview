from django.urls import path, include
from . import views

urlpatterns = [
path('', views.index, name='index'), # Path for the index page.
path('shop/', views.shop, name='shop'), # Path for the Online shop page.
path('contact/', views.contact, name='contact'), # Path for the Contact Us page.
]
