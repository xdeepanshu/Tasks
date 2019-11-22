from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from django.contrib import admin

from tasks.models import Task



class TaskAdmin(ModelAdmin):
    """
    TaskAdmin describes the Task model used in admin interface
    """
    model = Task
    menu_label = "Tasks"
    menu_icon = "placeholder"
    menu_order = 290
    add_settings_to_menu = False
    exclude_from_explorer = False
    list_display = ("task_description", )
    search_fields = ("task_description", )

modeladmin_register(TaskAdmin)


admin.site.register(Task)