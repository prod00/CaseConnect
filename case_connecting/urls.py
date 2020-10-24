from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView,\
    PostUpdateView, PostDeleteView, UserPostListView, search, PostApplyView, PostApplicationsListView, PostApplicantsListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="case_connecting-home"),
    path('reults', search, name="case_connecting-search"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/<int:pk>/apply/', PostApplyView.as_view(), name="post-apply"),
    path('applications/<str:username>/', PostApplicationsListView.as_view(template_name='case_connecting/applications_page.html'), name="case_connecting-applications"),
    path('applicants/<str:username>/', PostApplicantsListView.as_view(template_name='case_connecting/applicants.html'), name="case_connecting-applicants"),
    path('about/', views.about, name="case_connecting-about"),
    path('activity/<str:username>/', PostApplicantsListView.as_view(template_name='case_connecting/activity.html'), name="case_connecting-activity"),

]
