from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from users.models import *

# Create your views here.
def home(request):
    return render(request, 'task/index.html')

################### Task Page View ################
@login_required(login_url='login')
def createTask(request):
    profile = request.user.profile
    form = TaskCreationForm()
    tasks = profile.task_set.exclude(status="🙌Completed").order_by('-updated_time_stamp')

    task_num = tasks.count()
    date = datetime.now()
    weekday = date.strftime("%A")
    month = date.strftime("%b")
    day = date.strftime("%d")  

    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.account_owner = profile
            task.save()

            messages.success(request, 'New Task created successfully')
            return redirect('tasks')
    
    context = {'form': form, 'tasks': tasks, 'task_num': task_num, 'weekday': weekday, 'month': month, 'day': day}
    return render(request, 'task/task.html', context)

################### Completed Task Page View ################
@login_required(login_url='login')
def completedTask(request):
    completed_task = request.user.profile.task_set.filter(status="🙌Completed").order_by('-updated_time_stamp')

    # num of completed tasks
    task_arr = []
    for task in completed_task:
        task_arr.append(task)
    no_completed_task = len(task_arr)

    if request.method == 'POST':
        completed_task.delete()
        messages.success(request, 'Task deleted successfully')
        return redirect('completed-task')
    
    context = {'completed_task': completed_task, 'task_arr': task_arr, 'no_completed_task': no_completed_task}
    return render(request, 'task/completed-task.html', context)

################### Update & Delete Task Page View ################
@login_required(login_url='login')
def update_and_delete_task(request, pk):
    profile = request.user.profile
    task = profile.task_set.get(id=pk)
    display_note = task.note_set.all()  

    form = TaskCreationForm(instance=task)
    if request.method == 'POST':
        if 'submitNote' in request.POST:
            message = Note.objects.create(
                user = profile,
                new_note = request.POST.get('note'),
                task = task,
            )
            task.getNotesCount
            return redirect('update-task', pk=task.id)

        else:
            form = TaskCreationForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                messages.success(request, 'Task successfully updated!')
                return redirect('tasks')
            else:
                task.delete()
                messages.error(request, 'Task deleted successfully!')
                return redirect('tasks')

    context = {'profile': profile, 'task': task, 'display_note': display_note, 'form': form}
    return render(request, 'task/update_and_delete.html', context)








