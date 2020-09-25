from django.shortcuts import render
from .models import Post


#home page for case_connecting
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'case_connecting/home.html', context)

#about page for case_connecting
def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'case_connecting/about.html', context)