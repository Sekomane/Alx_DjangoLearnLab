from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
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

        path(
        "posts/<int:post_id>/comments/new/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),

    path(
        "comments/<int:pk>/update/",
        CommentUpdateView.as_view(),
        name="comment-update",
    ),

    path(
        "comments/<int:pk>/delete/",
        CommentDeleteView.as_view(),
        name="comment-delete",
    ),

]
