from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks', views.createTask, name='tasks'),
    path('completed-task', views.completedTask, name='completed-task'),
    path('update-task/<str:pk>', views.update_and_delete_task, name='update-task'),
]