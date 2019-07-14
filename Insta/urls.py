from django.contrib import admin
from django.urls import path, include
from Insta.views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]

