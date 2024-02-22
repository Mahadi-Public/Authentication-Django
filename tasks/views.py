from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from tasks.forms import TaskListForm
from django.contrib import messages
from tasks.models import TaskList
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def home_page(request):
    return render(request, 'tasks/index.html')

@login_required
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

@login_required
def tasks_list(request):
    
    query = request.GET.get('search')
    queryset = TaskList.objects.filter(user=request.user)
    
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q (category__icontains=query) |
            Q (price__icontains=query)
        )
    
    paginator = Paginator(queryset, 5) # show 5 list in pages
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) 
    
    serial_number = (page_obj.number - 1) * page_obj.paginator.per_page + 1
    
    for index, item in enumerate(page_obj, start=serial_number):
        item.serial_number = index    
        
    context = {
        "page_obj"  : page_obj
    }
    
    return render (request, 'tasks/tasks_froms_list.html', context)


@login_required
def tasks_list_details(request, id):
    
    queryset = TaskList.objects.get(id=id)
    context = {
        "queryset" : queryset
    }
    
    return render (request, 'tasks/tasks_list_details.html', context)

@login_required
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

@login_required
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
    



