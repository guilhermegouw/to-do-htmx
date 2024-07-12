from django.urls import path

from .views import (
    add_todo,
    add_todo_form,
    delete_todo,
    edit_todo,
    edit_todo_form,
    mark_todo_complete,
    todo_list,
)

urlpatterns = [
    path("", todo_list, name="todo_list"),
    path("add/", add_todo, name="add_todo"),
    path("add/form/", add_todo_form, name="add_todo_form"),
    path(
        "mark_complete/<int:todo_id>/",
        mark_todo_complete,
        name="mark_todo_complete",
    ),
    path("delete/<int:todo_id>/", delete_todo, name="delete_todo"),
    path("edit_form/<int:todo_id>/", edit_todo_form, name="edit_todo_form"),
    path("edit/<int:todo_id>/", edit_todo, name="edit_todo"),
]
