import datetime

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, StudentList
from .forms import TaskForm, StudentForm
import random
import string
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


def projecthomepage(request):
    return render(request, 'adminapp/ProjectHomePage.html')


def printpagecall(request):
    return render(request, 'adminapp/print.html')


def printpagelogic(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        print(f"User Input: {user_input}")
    a1 = {'user_input': user_input}
    return render(request, 'adminapp/print.html', a1)


def exceptionpagecall(request):
    return render(request, 'adminapp/exceptions.html')


def exceptionpage(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/exceptions.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/exceptions.html')


def randompagecall(request):
    return render(request, 'adminapp/RandomExample.html')


def randomlogic(request):
    global ran
    if request.method == 'POST':
        num = int(request.POST['num'])
        ran = ''.join(random.sample(string.digits, k=num))
    a1 = {'ran': ran}
    return render(request, 'adminapp/RandomExample.html', a1)


def calculatorpagecall(request):
    return render(request, 'adminapp/calculators.html')


def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculators.html', {'result': result})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'adminapp/To_Do_List.html', {'form': form, 'tasks': tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk)
    task.delete()
    return redirect('add_task')


def datetimepagecall(request):
    return render(request, 'adminapp/datetime.html')


def datetimelogic(request):
    if request.method == 'POST':
        number1 = int(request.POST['date1'])
        x= datetime.datetime.now()
       # print(x + datetime.timedelta(days=-89))
        result = x + datetime.timedelta(days=number1)
    return render(request, 'adminapp/datetime.html', {'result': result})


def registerpagecall(request):
    return render(request, 'adminapp/register.html')


def loginpagecall(request):
    return render(request, 'adminapp/login.html')


def registerpagelogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']  # Updated field name
        last_name = request.POST['last_name']    # Added last_name field
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirm-password']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,   # Added last_name to the user creation
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/ProjectHomePage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')


def loginpagelogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # Check the length of the username
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/login.html')
    else:
        return render(request, 'adminapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})


def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})
