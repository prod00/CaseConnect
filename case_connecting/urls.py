from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView,\
    PostUpdateView, PostDeleteView, UserPostListView, search,\
    PostApplyView, PostApplicationsListView, PostApplicantsListView,\
    SaveView, SavedListView, SaveDeleteView, CurrentUserPostListView,\
    PostApplicationDeleteView, PostApplicantDeleteView, ChatView, ChatListView, SpecificChatListView

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="case_connecting-home"),
    path('reults', search, name="case_connecting-search"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/<int:pk>/unsave/', SaveDeleteView.as_view(), name="post-unsave"),
    path('post/<int:pk>/apply/', PostApplyView.as_view(), name="post-apply"),
    path('post/<int:pk>/save/', SaveView.as_view(), name="post-save"),
    path('applications/', PostApplicationsListView.as_view(template_name='case_connecting/applications_page.html'), name="case_connecting-applications"),
    path('post/<int:pk>/delete-application/', PostApplicationDeleteView.as_view(), name="post-delete-application"),
    path('post/<int:pk>/delete-applicant/', PostApplicantDeleteView.as_view(template_name='case_connecting/applicant_confirm_delete.html'), name="post-delete-applicant"),
    path('post/<int:pk>/chat-application/',
         ChatView.as_view(),
         name="post-chat-applicant"),
    path('applicants/', PostApplicantsListView.as_view(template_name='case_connecting/applicants.html'), name="case_connecting-applicants"),
    path('saved/',
         SavedListView.as_view(template_name='case_connecting/saved.html'),
         name="case_connecting-saved"),
    path('post-list', CurrentUserPostListView.as_view(), name="case_connecting-posts"),
    path('chats/',
         ChatListView.as_view(template_name='case_connecting/chat_list_view.html'),
         name="case_connecting-chats"),
    path('chat/<int:pk>/',
         SpecificChatListView.as_view(template_name='case_connecting/specific_chat.html'),
         name="case_connecting-chat"),
    path('about/', views.about, name="case_connecting-about"),


]
