from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


# Test suite for Book API views
class BookAPITestViews(APITestCase):

    def setUp(self):
        """
        Set up test data before each test runs.
        Creates:
        - test user
        - test author
        - test book
        """

        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )

        # Create author
        self.author = Author.objects.create(
            name="George Orwell"
        )

        # Create book
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])


    # TEST READ OPERATIONS

    def test_list_books(self):
        """Test retrieving all books"""

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_retrieve_book(self):
        """Test retrieving single book"""

        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")


    # TEST CREATE OPERATION

    def test_create_book_authenticated(self):
        """Test creating book with authentication"""

        self.client.login(
            username='testuser',
            password='testpassword123'
        )

        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_book_unauthenticated(self):
        """Test creating book without authentication fails"""

        data = {
            "title": "Brave New World",
            "publication_year": 1932,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    # TEST UPDATE OPERATION

    def test_update_book_authenticated(self):
        """Test updating book with authentication"""

        self.client.login(
            username='testuser',
            password='testpassword123'
        )

        data = {
            "title": "1984 Updated",
            "publication_year": 1949,
            "author": self.author.id
        }

        response = self.client.put(self.update_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # TEST DELETE OPERATION

    def test_delete_book_authenticated(self):
        """Test deleting book with authentication"""

        self.client.login(
            username='testuser',
            password='testpassword123'
        )

        response = self.client.delete(self.delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    # TEST FILTERING

    def test_filter_books_by_year(self):
        """Test filtering books by publication year"""

        response = self.client.get(
            self.list_url + '?publication_year=1949'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # TEST SEARCHING

    def test_search_books(self):
        """Test searching books by title"""

        response = self.client.get(
            self.list_url + '?search=1984'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # TEST ORDERING

    def test_order_books(self):
        """Test ordering books"""

        response = self.client.get(
            self.list_url + '?ordering=title'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
