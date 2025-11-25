from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



# Create your views here.



# index: pagina de bienvenida
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

# edit: pagina para editar las tareas
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("tasks:detail", task_id = task.id)
    
    else:
        # Si es un GET, mostramos el formulario precargado con la tarea
        form = TaskForm(instance=task)
    return render(request, "tasks/edit.html", {"form":form, "task":task})

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tasks:main")
    
    else:
        form = TaskForm()
    
    return render(request, "tasks/add_task.html", {"form": form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect("tasks:main")


#login: pagina para logearte como usuario
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("tasks:main")
            else:
                form.add_error(None, "Usuario o contraseña incorrectos.")
    else:
        form = LoginForm()
    return render(request, "tasks/login.html", {"form":form})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            return redirect("tasks:index")
    else:
        form = RegisterForm()
    return render(request, "tasks/register.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect("tasks:index")