from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'tasks/index.html', {'tasks': tasks, 'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('index')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

def toggle_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.concluida = not task.concluida
    task.save()
    return redirect('index')
