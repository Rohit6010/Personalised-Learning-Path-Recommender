from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.handleSignup),
    path('login/', views.handleLogin),
]