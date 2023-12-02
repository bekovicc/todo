from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TodoForm
from .models import Todo

# Create your views here.


def detailpageview(request, pk):
    todo = Todo.objects.filter(id=pk).first()
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)

def deletetodo(request, pk):
    todo = Todo.objects.filter(id=pk).first()
    todo.delete()
    return redirect('listpage')


def homepageview(request):
    return render(request, 'index.html')


def listpageview(request):
    todo_list = Todo.objects.all()
    context = {
        'todolist': todo_list
    }
    return render(request, 'list.html', context)


def todo(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todo_list.html', context)


def todo_add(request):
    todo_list = Todo.objects.order_by('-date')

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listpage')
        else:
            form = TodoForm()
    form = TodoForm()
    return render(request, 'todo_create.html', {'form': form})


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("listpage")
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo_edit.html', {'form': form})
