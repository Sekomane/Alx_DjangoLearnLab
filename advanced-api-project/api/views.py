from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer



# List all books
# List all books with filtering, searching, and ordering
class BookListView(generics.ListAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Filtering fields
    filterset_fields = [
        'title',
        'publication_year',
        'author'
    ]

    # Search fields
    search_fields = [
        'title',
        'author__name'
    ]

    # Ordering fields
    ordering_fields = [
        'title',
        'publication_year'
    ]

    # Default ordering
    ordering = ['title']



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
