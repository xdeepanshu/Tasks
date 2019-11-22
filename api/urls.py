from django.urls import path
from api.views import ListTaskView, DoneTasksView, PendingTasksView, create_new_task, delete_task

urlpatterns = [
    path('', ListTaskView.as_view(), name="all-tasks"),
    path('done/', DoneTasksView.as_view(), name="all-done-tasks"),
    path('pending/', PendingTasksView.as_view(), name="all-pending-tasks"),
    path('create/', create_new_task, name="create-task"),
    path('delete/<int:pk>', delete_task, name="delete-task"),

]


