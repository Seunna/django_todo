from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
def list_todos(request):
    todos = Todo.objects.all()
    # print(todos)
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    

@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    return Response(f'Successfully deleted {pk}')

@api_view(['PATCH'])
def update_todo(request, primary_key):
    todo = get_object_or_404(Todo, id=primary_key)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.date)