from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})


def add_todo_form(request):
    return render(request, "todos/add_todo_form.html")


def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Todo.objects.create(title=title, description=description)
        return redirect("todo_list")
    return HttpResponse(status=400)


def mark_todo_complete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("todo_list")


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect("todo_list")


def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        todo.title = title
        todo.description = description
        todo.save()
        return redirect("todo_list")
    return HttpResponse(status=400)


def edit_todo_form(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, "todos/edit_todo_form.html", {"todo": todo})
