from django.shortcuts import render
from tasks.models import Tasks
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    View,
    DeleteView,
    UpdateView,
)


def index(request):
    return render(request, "index.html")


class TasksListView(ListView):  # список незавершенных задач
    model = Tasks
    context_object_name = "tasks_"
    queryset = Tasks.objects.filter(completed=False)
    template_name = "uncompleted.html"


class TasksCompleteListView(ListView):  # список завершенных задач
    model = Tasks
    context_object_name = "tasks_compl_"
    queryset = Tasks.objects.filter(completed=True)
    template_name = "completed.html"


class TasksCreateView(CreateView):  # создание новой задачи
    model = Tasks
    fields = ["title"]
    template_name = "task_create.html"
    success_url = "/"


class TaskUpdateView(UpdateView):  # редактирование задачи
    model = Tasks
    template_name = "task_update.html"
    fields = ["title", "completed"]
    success_url = "/"


class TasksDeleteView(DeleteView):  # удаление задачи
    model = Tasks
    template_name = "task_delete.html"
    success_url = "/"
