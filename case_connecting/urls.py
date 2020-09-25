from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="case_connecting-home"),
    path('about/', views.about, name="case_connecting-about"),
]
