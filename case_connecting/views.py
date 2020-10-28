
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Post, Application, Save
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q

from django.core.mail import send_mail
from django.contrib import messages


# home page for case_connecting
def home(request):
    query = ""
    if request.method == 'GET':
        query = request.GET['q']

    context = {
        'query': str(query),
        'posts': Post.objects.all(),
    }
    return render(request, 'case_connecting/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'case_connecting/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # the most recent available jobs will be moved to the top
    paginate_by = 8  # the number of posts per page


class UserPostListView(ListView):
    model = Post
    template_name = 'case_connecting/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 8  # the number of posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(recruiter=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['position', 'knowledge', 'content', 'pay']

    def form_valid(self, form):
        form.instance.recruiter = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['position', 'knowledge', 'content', 'pay']

    def form_valid(self, form):
        form.instance.recruiter = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.recruiter:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # sends user back to the home page once the post has been deleted

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.recruiter:
            return True
        else:
            return False


class PostApplyView(LoginRequiredMixin, CreateView):
    model = Application
    template_name = 'case_connecting/apply.html'
    fields = ['message']

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        post_id = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        form.instance.post = Post.objects.get(pk=post_id.id)
        return super().form_valid(form)


class PostApplicationsListView(ListView):
    model = Application
    context_object_name = 'applications'
    paginate_by = 8  # the number of posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Application.objects.filter(applicant=user).order_by('-date_applied')


class PostApplicantsListView(ListView):
    model = Application
    context_object_name = 'applications'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Application.objects.filter(post__recruiter=user).order_by('-date_applied')

class SaveView(LoginRequiredMixin, CreateView):
    model = Save
    template_name = 'case_connecting/save_form.html'
    fields = []

    def form_valid(self, form):
        form.instance.user = self.request.user
        post_id = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        form.instance.post = Post.objects.get(pk=post_id.id)
        super().form_valid(form)
        return redirect('/post/'+str(post_id.id))




class SavedListView(ListView):
    model = Save
    context_object_name = 'saved_posts'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Save.objects.filter(user=user).order_by('-date_saved')


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'case_connecting/about.html', context)


# search function
def search(request):
    template = 'case_connecting/post_list.html'
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(recruiter__username__icontains=query) |
                                Q(recruiter__first_name__icontains=query) |
                                Q(recruiter__last_name__icontains=query) |
                                Q(position__icontains=query) |
                                Q(knowledge__icontains=query) |
                                Q(pay__icontains=query))
    context = {
        'posts': posts
    }
    return render(request, template, context)


