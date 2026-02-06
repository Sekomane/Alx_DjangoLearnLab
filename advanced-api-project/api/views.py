from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# List all books
# Anyone can read, only authenticated users can write
class BookListView(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Allows read-only access for unauthenticated users
    permission_classes = [IsAuthenticatedOrReadOnly]


# Retrieve a single book
# Anyone can read
class BookDetailView(generics.RetrieveAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


# Create a new book
# Only authenticated users allowed
class BookCreateView(generics.CreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]


# Update an existing book
# Only authenticated users allowed
class BookUpdateView(generics.UpdateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]


# Delete a book
# Only authenticated users allowed
class BookDeleteView(generics.DestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]
