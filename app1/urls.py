from django.contrib import admin
from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from app1 import views

urlpatterns = [
    path('',PostListView.as_view(),name = 'Blog-home'),#for all posts
    path('user/<str:username>/',UserPostListView.as_view(),name = 'user-posts'),#particular user posts
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),#for specific post details
    path('post/new/',PostCreateView.as_view(),name = 'post-create'), #for creating post
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name = 'post-update'), #for updating a post
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post-delete'), #for updating a post
    path('details/',views.About,name = 'Blog-about'),

]