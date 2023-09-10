from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import UserRegisterForm
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(authenticate, email=email, password=password)
        login(request, user)
        messages.success(request, "You have been logged in Successfully")
        return redirect('home')
    return render(request, 'apps/home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out Successfully")
    return redirect('home')


def register_user(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email'].lower()
            #username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            destination = kwargs.get('next')
            if destination:
                return redirect(destination)
            messages.success(request, "You have been registered Successfully")
            return redirect('home')
            
        else:
            messages.success(request, "There is an Error in your form")
            return redirect('register')
    else:
        form = UserRegisterForm()
        return render(request, 'apps/register.html', {'form':form})