from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def main(request):
    return render(request, 'accounts/main.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:main')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:main')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def index(request):
    users = get_user_model().objects.all()
    context = {
        'users' : users
    }
    return render(request, 'accounts/index.html', context)

@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user':user,
    }
    return render(request, 'accounts/detail.html', context)

@login_required
def update(request, pk):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form
    }
    return render(request,'accounts/update.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:main')

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request) 
    return redirect('accounts:main')