from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return HttpResponse("Welcome to the UPI Management System!")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Safely get the username
        password = request.POST.get('password')  # Safely get the password
        
        if username and password:  # Check if both fields are filled
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Invalid credentials")
        else:
            return HttpResponse("Username and password are required.")
            
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
