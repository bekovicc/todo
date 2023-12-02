from django.urls import path, include
from .views import listpageview, homepageview, detailpageview, deletetodo, todo_add, todo_edit

urlpatterns = [
    path('todolist', listpageview, name='listpage'),
    path('todolist/<int:pk>/', detailpageview, name='detailpage'),
    path('', homepageview),
    path('delete/<int:pk>/', deletetodo, name='deletetodo'),
    path('add/', todo_add, name="todo_add"),
    path('todolist/<int:pk>/edit/', todo_edit, name='todo_edit')
]