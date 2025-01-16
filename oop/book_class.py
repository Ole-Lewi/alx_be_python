class Book:
    """A class to represent a book with title, author, and year."""

    def __init__(self, title, author, year):
        """Initialize the book with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the book is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: Returns a user-friendly string of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Returns a string that would recreate the book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

