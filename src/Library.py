from Book import Book
from Member import Member


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def __str__(self):
        return "welcome to library."

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} was added.")

    def remove_book(self, title):
        try:
            for book in self.books:
                if book.title == title:
                    self.books.remove(book)
                    print(f"{title} was deleted!")
        except Exception:
            print(f"{title} did not exist!")

    def list_books(self):
        if not self.books:
            print("no book here")
            return

        print("list of books:")
        for book in self.books:
            print(f"{book}")

    def add_member(self, name):
        if member.name == name:
            print(f"{name} already exist.")
            return
        self.members.append(name)
        print(f"{name} was successfully added.")

    def remove_member(self, name):
        try:
            self.members.remove(name)
            print(f"{name} was removed!")
        except Exception:
            print(f"{name} did not exist!")

    def list_members(self):
        for member in self.members:
            print(f"{member}")


if __name__ == "__main__":
    lib = Library()
    print(lib)
    book = Book("ss", "66", available=True)
    member = Member("ali", 1, book.title)
    lib.add_book(book)

    lib.add_member(member)
    lib.add_member(member)

    lib.list_books()
    lib.remove_book("ss")
    lib.list_books()
    lib.list_members()
