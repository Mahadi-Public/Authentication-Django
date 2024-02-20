from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from tasks.forms import TaskListForm
from django.contrib import messages
from tasks.models import TaskList

# Create your views here.

def home_page(request):
    return render(request, 'tasks/index.html')


def create_tasks(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST, request.FILES)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.user = request.user  # Assuming user is associated with the TaskList model
            task_list.save()
            messages.success(request, 'Form submitted successfully')
            return redirect('tasks_list')
        else:
            messages.warning(request, 'Form data is not vaild!')
    else:
        form = TaskListForm()
    return render(request, 'tasks/tasks_forms.html', {"form": form})


def tasks_list(request):
    
    queryset = TaskList.objects.all()
    context = {
        "queryset" : queryset
    }
    
    return render (request, 'tasks/tasks_froms_list.html', context)



def tasks_list_details(request, id):
    
    queryset = TaskList.objects.get(id=id)
    context = {
        "queryset" : queryset
    }
    
    return render (request, 'tasks/tasks_list_details.html', context)


def tasks_list_update(request, id):
    
    queryset = get_object_or_404(TaskList, id=id)
    if request.method == 'POST':
        form = TaskListForm(request.POST or request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Your data saved successfully")
            return redirect('tasks_list')
    else:
        form = TaskListForm(instance=queryset) 
        context = {
            'form': form,
            'queryset': queryset
        }
    return render(request, 'tasks/tasks_list_update.html', context)


def tasks_list_delete(request, id):
    
    queryset = get_object_or_404(TaskList, id=id)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, "Successfully deleted this task")
        return redirect('tasks_list')
    context = {
        'queryset': queryset
    }
    return render(request, 'tasks/tasks_list_delete.html', context)
    



