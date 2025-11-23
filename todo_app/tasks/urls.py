from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),      # /tasks/
    path("login/", views.login_view, name="login"), #/task/login/
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("inicio/", views.main, name="main"), # /tasks/inicio/
    path("<int:task_id>/", views.detail, name="detail"),
    path("<int:task_id>/edit/", views.edit_task, name="edit"), #/task/id/edit/
    

]
