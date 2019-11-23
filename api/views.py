from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks.models import Task 
from api.serializers import TasksSerializer
from django.shortcuts import get_object_or_404
from rest_framework.schemas import AutoSchema
import coreapi


class ListTaskView(generics.ListAPIView):
    """
    Returns all the tasks
    """
    serializer_class = TasksSerializer
    
    #For showing the get request param in swagger
    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("order", 
            required=False,
            location='query',
            description='describe the ordering either asc or desc. desc by default'),
        ]
    )
    
    def get_queryset(self):
        """
        This view should return a list of all the tasks for
        order portion of the URL.
        """

        order = self.request.query_params.get('order', None)
        print(order)
        if order == "asc":
            tasks = Task.objects.order_by('finish_time')
            return tasks
        else:
            tasks = Task.objects.order_by('-finish_time')
            return tasks
            


class DoneTasksView(generics.ListAPIView):
    """
    Returns all the completed tasks
    """
    serializer_class = TasksSerializer

    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("order", 
            required=False,
            location='query',
            description='describe the ordering either asc or desc. desc by default'),
        ]
    )

    def get_queryset(self):
        """
        This view should return a list of all the tasks for
        order portion of the URL.
        """
        tasks = Task.objects.filter(completed=True)

        order = self.request.query_params.get('order', None)
    
        if order == "asc":
            return tasks.order_by('finish_time')
        else:
          return tasks.order_by('-finish_time')

class PendingTasksView(generics.ListAPIView):
    """
    Returns all the pending tasks
    """
    serializer_class = TasksSerializer

    schema = AutoSchema(
        manual_fields=[
            coreapi.Field("order", 
            required=False,
            location='query',
            description='describe the ordering either asc or desc. desc by default'),
        ]
    )

    def get_queryset(self):
        """
        This view should return a list of all the tasks for
        order portion of the URL.
        """
        tasks = Task.objects.filter(completed=False)
        order = self.request.query_params.get('order', None)
        
        if order == "asc":
            return tasks.order_by('finish_time')
        else:
          return tasks.order_by('-finish_time')





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



