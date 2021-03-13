from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskItem(DetailView):
    model = Task
    template_name = 'task_item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context