class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title}|{self.author}|{self.available}"


class Member:
    def __init__(self, name, id, borrowed_books):
        self.name = name
        self.id = id
        self.borrowed_books = borrowed_books or []

    def __str__(self):
        borrowed_titles = []
        for book in self.borrowed_books:
            borrowed_titles.append(book.title)
        return f"{self.name}|{self.id}|{borrowed_titles}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.filename = "libstate.txt"

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return print(f"{book.title} was added to Library.")
        else:
            print(f"{book.title} already exists!")

    def remove_book(self, book):
        if book not in self.books:
            print(f"{book.title} does not exists!")
        else:
            self.books.remove(book)
            print(f"{book.title} was removed.")

    def list_books(self):
        for book in self.books:
            print(book)
        if not self.books:
            print("There is no book here...")

    def add_member(self, member):
        for m in self.members:
            if m.id == member.id:
                print(f"{member.name} with id:{member.id} already exists.")
                return
        self.members.append(member)
        print(f"{member.name} was added.")


if __name__ == "__main__":
    book1 = Book("book1", "author1")
    book2 = Book("book2", "author2")

    member1 = Member("member1", 1, None)
    member2 = Member("member2", 2, None)

    lib = Library()
    lib.add_book(book1)
    # lib.add_book(book2)
    # lib.list_books()
    lib.add_member(member1)
    lib.add_member(member2)

    print()