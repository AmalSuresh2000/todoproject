from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from.models import Task
from .forms import TodoForm

#using class todolist view
from django.views.generic import ListView #home.html
from django.views.generic.detail import DetailView #detail
from django.views.generic.edit import UpdateView,DeleteView #edit.html

#

# Create your views here.
# using class 'todolsit view'

class Tasklistview(ListView):

    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'Task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('Task','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1': task1})

# def details(request):
#     return render(request,'detail.html',)

def details(request):
    task=Task.objects.all()
    return render(request,'detail.html',{'task':task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'post':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

# update code django video 74
def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})
