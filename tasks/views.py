from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import TaskForm
from .models import task

import datetime

# Create your views here.

@login_required
def taskList(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    tasksDoneRecently = task.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()
    
    tasksDone = task.objects.filter(done='done', user=request.user).count()
    
    tasksDoing = task.objects.filter(done='doing', user=request.user).count()

    if search:    
        Task_list = task.objects.filter(title__icontains=search, user=request.user)

    elif filter:
        Task_list = task.objects.filter(done=filter, user=request.user)

    else:
        Task_list = task.objects.all().order_by('-created_at').filter(user=request.user)
        
    paginator = Paginator(Task_list, 3)
    page = request.GET.get('page')
    Task = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': Task, 'tasksrecently': tasksDoneRecently, 'tasksDone': tasksDone, 'tasksDoing': tasksDoing})  


@login_required
def taskView(request, id):
    Task = get_object_or_404(task, pk=id)
    return render(request, 'tasks/task.html', {"task": Task})


@login_required
def newtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            Task = form.save(commit=False)
            Task.done = 'doing'
            Task.user = request.user
            Task.save()

            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {"form": form})


@login_required
def editTask(request, id):
    Task = get_object_or_404(task, pk=id)
    form = TaskForm(instance=Task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=Task)
        
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'tasks/editTask.html', {'form': form, 'task': Task})   

    else:
        return render(request, 'tasks/editTask.html', {'form': form, 'task': Task})


@login_required
def deleteTask(request, id):
    Task = get_object_or_404(task, pk=id)
    Task.delete()
    messages.info(request, "Tarefa deletada com sucesso!")

    return redirect('/')


@login_required
def changeStatus(request, id):
    Task = get_object_or_404(task, pk=id)

    if Task.done == 'doing':
        Task.done = 'done'
    else:
        Task.done = 'doing'

    Task.save()
    return redirect('/')


def helloworld(request):
    return HttpResponse("Hello, World!")


def yourname(request, name):
    return render(request, 'tasks/yourname.html', {"nome": name})
    