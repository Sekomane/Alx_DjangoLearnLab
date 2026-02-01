from django.db import models
from django.conf import settings


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title





class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE, related_name="librarian"
    )

    def __str__(self):
        return self.name
