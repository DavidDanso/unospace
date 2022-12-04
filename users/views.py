from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
################### Create Account Page View ################
def createAccountPage(request):
    if request.user.is_authenticated:
        return redirect('tasks')

    form = createUserAccount()
    if request.method == 'POST':
        form = createUserAccount(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, f'Welcome {user.username}! a mail has been sent to your email address')
            login(request, user)
            return redirect('tasks')
        else:
            messages.error(request, 'An error occurred while registering!')

    context = {'form': form}
    return render(request, 'users/create-account.html', context)

################### Login Page View ################
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('tasks')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User not found')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tasks')
    return render(request, 'users/login.html')

################### Logout Page View ################
def logoutPage(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')

################### User Profile Page View ################
@login_required(login_url='login')
def userProfile(request):
    user = request.user.profile
    form = UserProfileForm(instance=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('tasks')

    context = {'user': user, 'form': form}
    return render(request, 'users/profile.html', context)








