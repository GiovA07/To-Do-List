from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),      # /tasks/
    path("inicio/", views.main, name="main"), # /tasks/inicio/
    path("<int:task_id>/", views.detail, name="detail"),
    path("<int:task_id>/edit/", views.edit_task, name="edit"), #/task/id/edit/
]
