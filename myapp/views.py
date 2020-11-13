from django.shortcuts import render
from . import models
from myapp.models import Todo
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    # reverse the items
    todo_obj = models.Todo.objects.all().order_by("-date")
    return render(request, 'main/index.html', {
        "todo_obj": todo_obj
    })


def add_todo(request):
    content = request.POST.get('content')
    models.Todo.objects.create(text=content)
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
