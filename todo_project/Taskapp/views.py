from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    return render(request, 'task_list.html', {'tasks': tasks,'form':form, 'total_tasks': total_tasks, 'completed_tasks': completed_tasks})

def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('/')
    return render(request, 'task_list.html')

def update(request,id):
    task=Task.objects.get(id=id)
    f=TaskForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
