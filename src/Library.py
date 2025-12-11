class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"Book: {self.title}, author: {self.author}, available: {self.available}"


class Member:
    def __init__(self, name, id, borrowed_books):
        self.name = name
        self.id = id
        self.borrowed_books = borrowed_books or []

    def __str__(self):
        borrowed_titles = []
        for book in self.borrowed_books:
            borrowed_titles.append(book.title)

        return f"name: {self.name}, id: {self.id}, borrowed books: {borrowed_titles}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.file_name = "libstate.txt"

    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} was added.")

    def remove_book(self, book):
        for b in self.books:
            if b.title == book.title:
                self.books.remove(b)
                print(f"{book.title} was removed.")
                return

        raise ValueError(f"{book.title} does not exist!")

    def list_books(self):
        for book in self.books:
            print(f"{book}")
        if not self.books:
            print("no book here!")

    def add_member(self, member):
        for m in self.members:
            if m.id == member.id:
                print(f"{member.name} already exist")
                return
        self.members.append(member)
        print(f"{member.name} was added.")

    def remove_member(self, member):
        for m in self.members:
            if m.id == member.id:
                self.members.remove(m)
                print(f"{member.name} was removed.")
                return

        raise ValueError(f"{member.name} was not a member!")

    def list_members(self):
        for member in self.members:
            print(f"{member}")
        if not self.members:
            print("no member yet...")
            return

    def borrow_book(self, book, member):
        if book not in self.books:
            raise ValueError(f"{book.title} is not found")

        if member not in self.members:
            raise ValueError(f"{member.name} not in members")

        if not book.available:
            raise ValueError(f"{book.title} is not available!")

        book.available = False
        member.borrowed_books.append(book)
        print(f"{member.name} has borrowed {book.title}.")

    def return_book(self, book, member):
        if book not in self.books:
            raise ValueError(f"{book.title} is not found")

        if member not in self.members:
            raise ValueError(f"{member.name} not in members")

        if book.available:
            raise ValueError(f"{book.title} is available!")

        book.available = True
        member.borrowed_books.remove(book)
        print(f"{member.name} has returned {book.title}.")

    def save_state(self):
        with open(self.file_name, "w") as f:
            # save book
            f.write("BOOKS:\n")
            for book in self.books:
                f.write(f"{book.title}|{book.author}|{book.available}\n")

            # save members
            f.write("MEMBERS:\n")
            for member in self.members:
                borrowed = []
                for book in member.borrowed_books:
                    borrowed.append(book.title)
                    f.write(f"{member.name}|{member.id}|{borrowed}\n")

    def load_state(self):
        with open(self.file_name, "r") as f:
            # load books
            lines = f.readlines()
            for line in lines:
                if line.strip():
                    self.books = line.strip()

            # load members
            lines = f


if __name__ == "__main__":
    lib = Library()
    book1 = Book("book1", "author1")
    book2 = Book("book2", "author2")
    member1 = Member("Soroosh", 1, None)
    member2 = Member("Soroosh2", 2, None)
    lib.add_book(book1)
    lib.add_book(book2)

    lib.add_member(member1)
    lib.add_member(member2)

    lib.borrow_book(book1, member1)

    # lib.list_books()
    lib.list_members()
    lib.save_state()

    # lib.return_book(book1, member1)
    # lib.list_books()
    # lib.list_members()
