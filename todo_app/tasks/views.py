from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.http import Http404
from .forms import TaskForm


# Create your views here.



# index: página de bienvenida
def index(request):
    return render(request, "tasks/index.html")

# main: lista de tareas
def main(request):
    latest_tasks_list = Task.objects.order_by("-created_at")[:5]
    context = {"latest_tasks_list": latest_tasks_list}
    return render(request, "tasks/main.html", context)

# detalle de una tarea
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "tasks/detail.html", {"task": task})

# index: página de bienvenida
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("task:detail", task_id = task_id)
    
    else:
        # Si es un GET, mostramos el formulario precargado con la tarea
        form = TaskForm(instance=task)
    return render(request, "task/edit.html", {"form":form, "task":task})