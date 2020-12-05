from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Post, Application, Save, Chat
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages


# home page for case_connecting
def home(request):

    context = {
        'posts': Post.objects.all(),  # home page has all the posts available
    }
    return render(request, 'case_connecting/home.html', context)

# This view is for the home page
class PostListView(ListView):
    model = Post
    template_name = 'case_connecting/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # the most recent available jobs will be moved to the top
    paginate_by = 15  # the number of posts per page

# This view is for a specific users posts
class UserPostListView(ListView):
    model = Post
    template_name = 'case_connecting/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 8  # the number of posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(recruiter=user).order_by('-date_posted')

# This view is for a posts detail view
class PostDetailView(DetailView):
    model = Post

# This view is for creating a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['position', 'knowledge', 'content', 'pay']  # All the fields the user needs to fill in

    def form_valid(self, form):
        form.instance.recruiter = self.request.user  # Making the current user the recruiter of the post
        return super().form_valid(form)

# This view is for updating a post
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['position', 'knowledge', 'content', 'pay']  # All the fields the user can update

    def form_valid(self, form):
        form.instance.recruiter = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.recruiter:  # The "test" to make sure the user is who they say they are.
            return True
        else:
            return False

# This view is for deleting a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/post-list'  # Where the user should get redirected when they delete a post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.recruiter:
            return True
        else:
            return False

# This view is for applying to a post
class PostApplyView(LoginRequiredMixin, CreateView):
    model = Application
    template_name = 'case_connecting/apply.html'
    fields = ['message']

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        post_id = get_object_or_404(Post, pk=self.kwargs.get('pk'))  # getting the specific post with the id from the url
        form.instance.post = Post.objects.get(pk=post_id.id)
        messages.success(self.request,
                         "Successfully Applied To '" + str(form.instance.post.position) + "'")
        return super().form_valid(form)

# This view is for the applications the user has sent
class PostApplicationsListView(ListView):
    model = Application
    context_object_name = 'applications'
    paginate_by = 8  # the number of posts per page

    def get_queryset(self):
        request_user = self.request.user
        return Application.objects.filter(applicant=request_user).order_by('-date_applied')

# This view is for deleting applications
class PostApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Application
    success_url = '/applications'

    def test_func(self):
        application = self.get_object()
        if self.request.user == application.applicant:
            return True
        else:
            return False

# This view is for deleting applicants
class PostApplicantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Application
    success_url = '/applicants'

    def test_func(self):
        application = self.get_object()
        if self.request.user == application.post.recruiter:
            return True
        else:
            return False

# This view is for the users applicants
class PostApplicantsListView(ListView):
    model = Application
    context_object_name = 'applications'
    paginate_by = 8

    def get_queryset(self):
        request_user = self.request.user
        return Application.objects.filter(post__recruiter=request_user).order_by('-date_applied')

# This view is for saving a post
class SaveView(LoginRequiredMixin, CreateView):
    model = Save
    template_name = 'case_connecting/save_form.html'
    fields = []

    def form_valid(self, form):
        form.instance.user = self.request.user
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        form.instance.post = Post.objects.get(pk=post.id)
        super().form_valid(form)
        messages.success(self.request, "Successfully Saved '" + str(form.instance.post.position) + "' To Saved Posts")
        return redirect('/post/' + str(post.id))

# This view is for a users list of saved posts
class SavedListView(LoginRequiredMixin, ListView):
    model = Save
    context_object_name = 'saved_posts'
    paginate_by = 8

    def get_queryset(self):
        request_user = self.request.user
        return Save.objects.filter(user=request_user).order_by('-date_saved')

# This view is for deleting a saved post
class SaveDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Save
    success_url = '/saved/'  # sends user back to the Saved page once the post has been deleted

    def test_func(self):
        saved_post = self.get_object()
        if self.request.user == saved_post.user:
            return True
        else:
            return False

# This view is for the posts in the current users "posts" section
class CurrentUserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'case_connecting/current_user_posts.html'
    context_object_name = 'posts'
    paginate_by = 8  # the number of posts per page

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(recruiter=user).order_by('-date_posted')

# This view is for the chat box
class ChatView(LoginRequiredMixin, CreateView):
    model = Chat
    template_name = 'case_connecting/chat.html'
    fields = ['message']

    def form_valid(self, form):
        form.instance.sender = self.request.user
        application = get_object_or_404(Application, pk=self.kwargs.get('pk'))
        form.instance.app = Application.objects.get(pk=application.id)
        messages.success(self.request, "Successfully Sent Message")
        super().form_valid(form)
        newChat = Chat.objects.filter(app__id=application.id)
        first = newChat.first()

        return redirect('/chat/' + str(first.id))

# This view is for all the chat streams of the current user
class ChatListView(LoginRequiredMixin, ListView):
    model = Chat
    context_object_name = 'chats'
    paginate_by = 10

    def get_queryset(self):
        request_user = self.request.user
        chats = Chat.objects.filter(Q(app__applicant=request_user) |
                                    Q(app__post__recruiter=request_user)).order_by('-date_sent')

        combos = []
        chat_ids = []

        for chat in chats:
            # To make the chat stream unique I am combining the applicant user id and the post id to get the combo
            # and then testing whether that combo has been seen before.
            applicant = chat.app.applicant
            post_id = chat.app.post.id
            combo = str(applicant)+str(post_id)
            if combo not in combos:
                combos.append(combo)
                chat_ids.append(chat.id)


        filteredChats = []
        for chat_id in chat_ids:
            chat = Chat.objects.get(id=chat_id)
            filteredChats.append(chat)

        return filteredChats

# This view is for a specific chat with a unique person and job
class SpecificChatListView(LoginRequiredMixin, ListView):
    model = Chat
    context_object_name = 'chats'

    def get_queryset(self):
        request_user = self.request.user
        chat_obj = get_object_or_404(Chat, pk=self.kwargs.get('pk'))
        post_obj = get_object_or_404(Post, pk=chat_obj.app.post.id)
        applicant = chat_obj.app.applicant
        recruiter = chat_obj.app.post.recruiter

        return Chat.objects.filter(Q(app__applicant=request_user, app__post__recruiter=recruiter, app__post_id=post_obj.id) |
                                   Q(app__post__recruiter=request_user, app__applicant=applicant, app__post_id=post_obj.id)).order_by(
            '-date_sent')



def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'case_connecting/about.html', context)


def search(request):
    template = 'case_connecting/post_list.html'
    query = request.GET.get('q')  # query is what the user inputted in the filter bar
    posts = Post.objects.filter(Q(recruiter__username__icontains=query) |
                                Q(recruiter__first_name__icontains=query) |
                                Q(recruiter__last_name__icontains=query) |
                                Q(position__icontains=query) |
                                Q(knowledge__icontains=query) |
                                Q(pay__icontains=query))  # Checking if any of the sections have whatever the query is inside them
    context = {
        'posts': posts
    }
    return render(request, template, context)



