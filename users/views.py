from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, SignUpForm

# Sign-Up View
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})

# Login and Logout Views
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('book-list')  # Redirect to the book list after signing up
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
