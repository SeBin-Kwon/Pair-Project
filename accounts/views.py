from django.shortcuts import render, redirect
from . forms import CustomUserCreationForm

# Create your views here.
def main(request):
    return render(request, 'accounts/main.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:main')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)