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

    def add_member(self, member):
        for existing_member in self.members:
            if existing_member.name == member.name:
                print(f"{member.name} already exists!")
                return

        self.members.append(member)
        print(f"{member} was successfully added")

    def remove_member(self, member):
        try:
            for m in self.members:
                if m.name == member.name:
                    self.members.remove(m)
                    print(f"{m.name} was removed!")
        except Exception:
            print(f"{member} did not exist!")

    def list_members(self):
        if not self.members:
            print("no member here.")
            return
        for member in self.members:
            print(f"{member}")


if __name__ == "__main__":
    lib = Library()
    print(lib)
    book = Book("ss", "66", available=True)
    member = Member("ali", 1, book.title)
    member1 = Member("ali", 1, book.title)
    # lib.add_book(book)

    lib.add_member(member)
    lib.add_member(member1)

    # lib.list_books()
    # lib.remove_book("ss")
    # lib.list_books()
    lib.remove_member(member)
    lib.list_members()
