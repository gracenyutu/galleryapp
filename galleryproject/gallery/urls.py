from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gallery'),
    path('about/', views.about, name='about'),
    path('add/', views.addPhoto, name='add'),
    path('photo/<str:pk>', views.viewPhoto, name='photo'),
]