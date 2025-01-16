class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        """Initialize the book with title, author, and set it as not checked out."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            return False  # Book is already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Return the book and mark it as available."""
        self._is_checked_out = False

    def is_available(self):
        """Return whether the book is available or not."""
        return not self._is_checked_out

    def __str__(self):
        """Return the string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library, containing a collection of books."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False  # Book not found or already checked out

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False  # Book not found or already returned

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            print("\n".join(available_books))
        else:
            print("No available books.")

