from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Post, Application
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ApplicationForm


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
    fields = ['message', 'post']

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        #form.instance.post = Post.objects.get(id(Post))
        return super().form_valid(form)

class PostApplicationsListView(ListView):
    model = Application
    context_object_name = 'applications'
    #ordering = ['-date_posted']  # the most recent available jobs will be moved to the top
    #paginate_by = 8  # the number of posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Application.objects.filter(applicant=user)


class PostApplicantsListView(ListView):
    model = Application
    context_object_name = 'applications'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Application.objects.filter(post__recruiter=user)















# @login_required
# def apply(request):
#     context = {}
#     if request.POST.get("Apply"):
#         request.session["id"] = request.POST["Apply"]
#         apply_post = Post.objects.get(pk=request.session["id"])
#         context["apply_post"] = apply_post
#
#     if request.POST.get("Submit") and request.session["id"]:
#         form = ApplicationForm(request.POST)
#         print("form saved")
#         if form.is_valid():
#             print("form was valid")
#             id_num = int(request.session["id"])
#             post = Post.objects.get(pk=id_num)
#             email_body = str(request.POST['message'])
#             recruiter_email = str(post.recruiter.email)
#             position = post.position
#             recruiter_name = post.recruiter.get_full_name()
#             applicant_name = request.user.get_full_name()
#             email_subject = applicant_name + " has applied to your " + position + " position!"
#             send_mail(email_subject, email_body, 'CaseConnect2020@gmail.com', [recruiter_email])
#             messages.success(request, f'You have successfully applied to be a {position} for {recruiter_name}!')
#             return redirect('case_connecting-home')
#         else:
#             messages.warning(request, "The Message You Are Trying To Send Is Not Valid")
#     if bool(context):
#         return render(request, 'case_connecting/apply.html', context)
#     else:
#         return redirect('case_connecting-home')

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
                                Q(knowledge__icontains=query) |
                                Q(pay__icontains=query))
    context = {
        'posts': posts
    }
    return render(request, template, context)
