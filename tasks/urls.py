from django.urls import path

from . import views
 
urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('task/<int:id>/', views.taskView, name='task-view'),
    path('newTask', views.newtask, name='newtask'),
    path('editTask/<int:id>', views.editTask, name='edit-task'),
    path('deleteTask/<int:id>', views.deleteTask, name='delete-task'),
    path('changeStatus/<int:id>', views.changeStatus, name='change-status'),
    path('helloworld/', views.helloworld),
    path('yourname/<str:name>/', views.yourname),
]
