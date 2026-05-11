from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
# index: pagina de bienvenida
def index(request):
    if request.user.is_authenticated:
        return redirect("tasks:main")
    return render(request, "tasks/index.html")

# main: lista de tareas
@login_required
def main(request):
    state = request.GET.get("estado")
    tasks = Task.objects.filter(user=request.user)
    if state:
        tasks = tasks.filter(state = state)
    
    context = {"latest_tasks_list": tasks}
    return render(request, "tasks/main.html", context)

# detalle de una tarea
@login_required
def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    return render(request, "tasks/detail.html", {"task": task})

# edit: pagina para editar las tareas
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("tasks:detail", task_id = task.id)
    
    else:
        # Si es un GET, mostramos el formulario precargado con la tarea
        form = TaskForm(instance=task)
    return render(request, "tasks/edit.html", {"form":form, "task":task})

@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            msg = "La tarea '" + task.title + "' se agrego correctamente!." 
            messages.success(request, msg)
            return redirect("tasks:main")
    
    else:
        form = TaskForm()
    
    return render(request, "tasks/add_task.html", {"form": form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.delete()
    msg = "La tarea '" + task.title + "' fue eliminada." 
    messages.warning(request, msg)
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