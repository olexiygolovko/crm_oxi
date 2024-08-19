from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('record/<int:pk>/', views.customer_record, name='customer_record'),
    path('record/<int:pk>/add_task/', views.add_task_to_record, name='add_task_to_record'),
    path('record/<int:pk>/tasks/', views.view_tasks_for_record, name='view_tasks_for_record'),
    path('record/<int:pk>/add_task/', views.add_task_to_record, name='add_task_to_record'),
    path('record/<int:pk>/edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('record/<int:pk>/delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
         
]
