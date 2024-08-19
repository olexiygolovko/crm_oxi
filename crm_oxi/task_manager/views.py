from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm



@login_required
def tasks_main(request):
    tasks = Task.objects.all()
    return render(request, 'tasks_main.html', {'tasks': tasks})

@login_required
def add_task(request):
    form = TaskForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            messages.success(request, "Task added successfully!")
            return redirect('tasks_main')
    
    return render(request, 'add_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = TaskForm(request.POST or None, instance=task)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('tasks_main')
    
    return render(request, 'edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect('tasks_main')
