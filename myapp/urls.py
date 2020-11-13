from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('todo/', views.add_todo, name='todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete'),
]
