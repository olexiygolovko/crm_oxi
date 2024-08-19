from django.urls import path
from . import views

urlpatterns = [
    path('tasks_main/', views.tasks_main, name='tasks_main'),
    path('tasks_main/add_task/', views.add_task, name='add_task'),
    path('tasks_main/edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks_main/delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]