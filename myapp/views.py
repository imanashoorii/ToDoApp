from django.shortcuts import render
from . import models


# Create your views here.

def home(request):
    return render(request, 'main/index.html')


def add_todo(request):
    print(request.POST)

    content = request.POST.get('content')
    models.Todo.objects.create(text=content)
    print(content)
    return render(request, 'main/index.html')
