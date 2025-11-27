class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2025
        return current_year - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"
    
# Example usage:

book1 = Book("OIP Magazine", "Swathi",2001)
book2 = Book("Daily News", "Swathi.S",2005)

print("Book 1 Title:", book1.title)
print("Book 1 Author:", book1.author)
print("Book 1 Age of book:", book1.get_age(), "years")
print("Book 1 Summary:", book1.get_summary())

print()
print()

print("Book 2 Title:", book2.title)
print("Book 2 Author:", book2.author)
print("Book 2 Age of book:", book2.get_age(), "years")
print("Book 2 Summary:", book2.get_summary())