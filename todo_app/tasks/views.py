from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola mundo, este es la view de las tareas.")

def detail(request, task_id):
    return HttpResponse("Estas viendo la tarea  %s." % task_id)

