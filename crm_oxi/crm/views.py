from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, RecordCommentForm, RecordTaskForm
from .models import Record, RecordComment, RecordTask
from .filters import RecordFilter


def home(request):
    records = Record.objects.all()
    home = Record.objects.order_by('-created_at')
    
    record_filter = RecordFilter(request.GET, queryset=home)
    filtered_records = record_filter.qs
    
    paginator = Paginator(filtered_records, 15)  
    page_number = request.GET.get("page")  
    page_obj = paginator.get_page(page_number)
    
    context = {
        "records": page_obj.object_list,
        "record_filter": record_filter,
        "page_obj": page_obj
    }
    
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return render(request, 'home.html', context)
        else:
            messages.error(request, "There Was An Error Logging In, Please Try Again ...")
            return redirect('home')
    else:
        return render(request, 'home.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home') 
    else:
        form = SignUpForm()    
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

@login_required
def customer_record(request, pk):
    customer_record = Record.objects.get(id=pk)
    comments = RecordComment.objects.filter(record=customer_record).order_by('-created_at')
    tasks = RecordTask.objects.filter(record=customer_record).order_by('-due_date')

    form = RecordCommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.record = customer_record
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment has been added!")
            return redirect('customer_record', pk=pk)
    
    return render(request, 'record.html', {
        'customer_record': customer_record, 
        'comments': comments, 
        'tasks': tasks, 
        'form': form
    })

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect('home') 
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.error(request, "You Must Be Logged In...")
        return redirect('home') 

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.error(request, "You Must Be Logged In...")
        return redirect('home') 


@login_required
def view_tasks_for_record(request, pk):
    record = get_object_or_404(Record, id=pk)
    tasks = RecordTask.objects.filter(record=record).order_by('-due_date')
    return render(request, 'tasks.html', {'record': record, 'tasks': tasks})

@login_required
def add_task_to_record(request, pk):
    customer_record = get_object_or_404(Record, pk=pk)
    form = RecordTaskForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.record = customer_record
            task.save()
            messages.success(request, "Task added successfully!")
            return redirect('customer_record', pk=pk)
    
    return render(request, 'add_task.html', {'form': form, 'customer_record': customer_record})

@login_required
def edit_task(request, pk, task_id):
    customer_record = get_object_or_404(Record, pk=pk)
    task = get_object_or_404(RecordTask, pk=task_id)
    form = RecordTaskForm(request.POST or None, instance=task)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully!")
            return redirect('customer_record', pk=pk)
    
    return render(request, 'edit_task.html', {'form': form, 'customer_record': customer_record})

@login_required
def delete_task(request, pk, task_id):
    customer_record = get_object_or_404(Record, pk=pk)
    task = get_object_or_404(RecordTask, pk=task_id)
    task.delete()
    messages.success(request, "Task deleted successfully!")
    return redirect('customer_record', pk=pk)
