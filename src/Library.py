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
        self.borrowed_books = borrowed_books

    def __str__(self):
        return (
            f"name: {self.name}, id: {self.id}, borrowed books: {self.borrowed_books}"
        )


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} was added.")

    def remove_book(self, book):
        for b in self.books:
            if b.title == book.title:
                self.books.remove(b)
                print(f"{b.title} was removed.")
                return

        raise ValueError(f"{b.title} does not exist!")

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
                self.members.remove(member)
                print(f"{member.name} was removed.")
                return

        raise ValueError(f"{member.name} was not a member!")

    def list_members(self):
        for member in self.members:
            print(f"{member}")
        if not self.members:
            print("no member yet...")
            return
        

    def borrow_book(self,book):
        pass
    def return_book(self,book):
        pass


# class borrowe_return_book:


if __name__ == "__main__":
    lib = Library()
    book1 = Book("book1", "author1")
    member1 = Member("Soroosh", 1, None)
    member2 = Member("Soroosh2", 2, None)
    lib.add_book(book1)
    lib.list_books()
    lib.remove_book(book1)
    lib.list_books()

    lib.add_member(member1)
    lib.add_member(member2)
    lib.remove_member(member2)
    lib.remove_member(member1)
    lib.list_members()
