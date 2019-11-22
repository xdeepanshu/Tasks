from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks.models import Task 
from api.serializers import TasksSerializer
from django.shortcuts import get_object_or_404


class ListTaskView(generics.ListAPIView):
    """
    Returns all the tasks
    """
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

class DoneTasksView(generics.ListAPIView):
    """
    Returns all the completed tasks
    """
    queryset = Task.objects.filter(completed=True)
    serializer_class = TasksSerializer

class PendingTasksView(generics.ListAPIView):
    """
    Returns all the pending tasks
    """
    queryset = Task.objects.filter(completed=False)
    serializer_class = TasksSerializer


@api_view(['POST'])
def create_new_task(request):
    """
    Creates new task 
    """

    serializer = TasksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_task(request, pk):
    """
    Deletes a task of a given id
    """
    task = get_object_or_404(Task.objects.all(), pk=pk)
    task.delete()
    return Response({"message": "Task with id `{}` has been deleted.".format(pk)},status=status.HTTP_204_NO_CONTENT)



