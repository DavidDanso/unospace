from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.userProfile, name='profile'),
    path('login', views.loginPage, name='login'),
    path('create-account', views.createAccountPage, name='create-account'),
    path('logout', views.logoutPage, name='logout'),
]