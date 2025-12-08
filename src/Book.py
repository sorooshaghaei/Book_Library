class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        if self.available:
            status = "Available"
        else:
            status = "Not available"

        return f"Book title: '{self.title} , author: {self.author} and availability: {status}'"


if __name__ == "__main__":
    print("we are in book")

    book = Book("5","66",available=False)
    print(book)
    
