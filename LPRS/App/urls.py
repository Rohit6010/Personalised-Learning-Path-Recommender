from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.handleSignup),
    path('login/', views.handleLogin),
    path('logout/', views.logoutuser),
    path('test/<str:topic>/instruction', views.instruction, name="instruction"),
    path('test/<str:topic>/<str:level>', views.test, name="test"),
    path('testScore/<str:topic>/<str:level>', views.testScore, name="testScore"),
    path('levelDecider', views.levelDecider)
]