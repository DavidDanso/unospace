from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('routes/', views.getRoutes),

    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.getUsers),
    path('user/<str:pk>', views.getUser),

    path('tasks/', views.getTasks),
    path('task/<str:pk>', views.getTask),
    path('create-task/', views.createTask),

    path('delete-note/', views.deleteNote),
]