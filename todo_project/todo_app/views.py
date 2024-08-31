from django.shortcuts import render, HttpResponse, redirect,  get_object_or_404
from todo_app import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            u = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
            u.set_password(password)
            u.save()
            return redirect('/')
        else:
            context = {}
            context['error'] = "Password and Confirm Password do not match"
            return render(request, 'register.html', context)

def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            context = {}
            context['error'] = "Username and Password is incorrect"
            return render(request, 'login.html', context)
@login_required
def user_logout(request):
    logout(request)
    return redirect("/")

@login_required
def todo_list(request):
    if request.method == 'POST':
        # Get the data from the form
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Create a new task in the database
        Task.objects.create(title=title, description=description)
        
        # Redirect to the same page to see the new task
        return redirect('todo_list')

    # Fetch all tasks from the database
    tasks = Task.objects.all()

    return render(request, 'todo_list.html', {'tasks': tasks})





def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Retrieve the task by ID or return 404 if not found
    
    if request.method == 'POST':
        # Update the task with new data from the form
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = 'completed' in request.POST  # Update completion status based on form checkbox
        task.save()  # Save the updated task to the database
        
        return redirect('todo_list')  # Redirect to the To-Do List page
    
    # Render the edit page with the task data
    return render(request, 'edit_task.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Retrieve the task by ID or return 404 if not found
    task.delete()  # Delete the task from the database
    return redirect('todo_list')  # Redirect to the To-Do List page after deletion

def mark_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Retrieve the task by ID or return 404 if not found
    task.completed = True  # Mark the task as complete
    task.save()  # Save the changes to the database
    return redirect('todo_list')  # Redirect to the To-Do List page after marking as complete