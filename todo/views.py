from multiprocessing import context
from django.shortcuts import redirect,get_object_or_404, render 

from .models import Task

# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def delete(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    
    return redirect('home')

def undo(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=False 
    task.save()
    return redirect('home')


def edit(request,pk):
    task=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        updated_task = request.POST['task']
        task.task = updated_task
        task.save()
        return redirect('home')
    else:
        context={
            'task':task
        }
        return render(request, 'edit.html',context)

