from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [

    # List all posts
    path("posts/", PostListView.as_view(), name="post-list"),

    # Create new post
    path("post/new/", PostCreateView.as_view(), name="post-create"),

    # View single post
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    # Update post
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),

    # Delete post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

]
