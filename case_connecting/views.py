from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import send_mail

# home page for case_connecting
def home(request):
    request.session["email"] = None
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

class PostApplyView(UserPassesTestMixin, DetailView):
    model = Post
    template_name = 'case_connecting/apply.html'

    def test_func(self):
        post = self.get_object()
        if apply(self.request):
            if self.request.user != post.recruiter:
                send_mail(post.getPosition(), 'interested', 'CaseConnect2020@gmail.com', [str(post.recruiter.email)])
                return True
            else:
                return False

@login_required
def apply(request):
    if request.POST.get("recruiter_email"):
        print("post")
        request.session["email"] = request.POST["recruiter_email"]
    print("apply", request.POST.get("Submit"))
    print("email", request.session["email"])
    if request.POST.get("Submit") and request.session["email"]:
        print("works")
        send_mail('d', 'interested', 'CaseConnect2020@gmail.com', [str(request.session["email"])])
        return redirect('case_connecting-home')
    return render(request, 'case_connecting/apply.html')


# about page for case_connecting
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
                                Q(knowledge__icontains=query))
    context = {
        'posts': posts
    }
    return render(request, template, context)




