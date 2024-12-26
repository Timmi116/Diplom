from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('congratulations/', views.congratulations, name='congratulations'),
]