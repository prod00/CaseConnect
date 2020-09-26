from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


#home page for case_connecting
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'case_connecting/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'case_connecting/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # the most recent available jobs will be moved to the top

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['position', 'knowledge', 'content', 'pay']

    def form_valid(self, form):
        form.instance.recruiter = self.request.user
        return super().form_valid(form)



#about page for case_connecting
def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'case_connecting/about.html', context)