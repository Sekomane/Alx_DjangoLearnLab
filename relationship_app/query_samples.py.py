from relationship_app.models import Author, Library

# Query all books by a specific author
author = Author.objects.get(name="John Doe")
print("Books by author:")
print(author.books.all())

# List all books in a library
library = Library.objects.get(name="City Library")
print("\nBooks in library:")
print(library.books.all())

# Retrieve the librarian for a library
print("\nLibrarian:")
print(library.librarian)
