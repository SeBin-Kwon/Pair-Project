from django.shortcuts import render, redirect

from reviews.models import Review
from .forms import ReviewForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    context = {
        'form' : form
    }
    return render(request, 'reviews/create.html', context)

def index(request):
    review = Review.objects.order_by('-pk')
    context = {
        'review': review
    }
    return render(request, 'reviews/index.html', context)