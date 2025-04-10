from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm

def register_view(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('questions:home')  # Redirect to home if already logged in

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('questions:home')
        else:
            messages.error(request, "Registration failed. Please try again.")
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('questions:home')  # Redirect to home if already logged in
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('questions:home')
        else:
            messages.error(request, "Invalid username and password")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('questions:home')