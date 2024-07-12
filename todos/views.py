from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Todo


def is_htmx(request):
    return request.headers.get("HX-Request") == "true"


def todo_list(request):
    query = request.GET.get("query")
    if query:
        todos = Todo.objects.filter(title__icontains=query)
    else:
        todos = Todo.objects.all()
    if is_htmx(request):
        return render(
            request, "todos/todo_list_partial.html", {"todos": todos}
        )
    return render(request, "todos/todo_list.html", {"todos": todos})


def add_todo_form(request):
    return render(request, "todos/add_todo_form_partial.html")


def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Todo.objects.create(title=title, description=description)
        if is_htmx(request):
            todos = Todo.objects.all()
            return render(
                request, "todos/todo_list_partial.html", {"todos": todos}
            )
        return redirect("todo_list")
    return HttpResponse(status=400)


def mark_todo_complete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    if is_htmx(request):
        todos = Todo.objects.all()
        return render(
            request, "todos/todo_list_partial.html", {"todos": todos}
        )
    return redirect("todo_list")


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    if is_htmx(request):
        todos = Todo.objects.all()
        return render(
            request, "todos/todo_list_partial.html", {"todos": todos}
        )
    return redirect("todo_list")


def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        todo.title = title
        todo.description = description
        todo.save()
        if is_htmx(request):
            todos = Todo.objects.all()
            return render(
                request, "todos/todo_list_partial.html", {"todos": todos}
            )
        return redirect("todo_list")
    return HttpResponse(status=400)


def edit_todo_form(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, "todos/edit_todo_form_partial.html", {"todo": todo})
