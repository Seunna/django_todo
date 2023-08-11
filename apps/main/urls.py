from django.urls import path
from .views import list_todos, create_todo, delete_todo, update_todo

urlpatterns = [
    path('', list_todos),
    path('create/', create_todo),
    path('delete/<int:pk>/', delete_todo),
    path('update/<int:primary_key>/', update_todo)
]
