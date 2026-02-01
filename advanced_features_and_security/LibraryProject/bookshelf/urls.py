from django.urls import path
from .views import book_list, book_create, book_edit, book_delete

urlpatterns = [
    path("books/", book_list, name="book_list"),
    path("books/create/", book_create, name="book_create"),
    path("books/edit/<int:pk>/", book_edit, name="book_edit"),
    path("books/delete/<int:pk>/", book_delete, name="book_delete"),
]
