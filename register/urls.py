from django.urls import path
from . import views


urlpatterns = [
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
    path('login/outline/', views.outline, name='outline')
]