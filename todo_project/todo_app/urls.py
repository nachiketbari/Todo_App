
from django.urls import path
from todo_app import views
from todo_app.views import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('register/',views.user_register),
    path('login/', views.user_login),
    path('logout', views.user_logout),
    path('todo/', views.todo_list, name='todo_list'),
    path('todo/edit/<int:task_id>/', views.edit_task, name='edit_task'), 
    path('todo/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('todo/complete/<int:task_id>/', views.mark_complete, name='mark_complete'),  
    
]
