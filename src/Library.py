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
        for b in self.books:
            if b.title == book.title:
                print(f"{b.title} by author:{b.author} already exists.")
                return
        self.books.append(book)
        print(f"{book.title} was added.")

    def remove_book(self, book):
        for b in self.books:
            if b.title == book.title:
                self.books.remove(b)
                print(f"{b.title} was removed.")
                return
        print(f"{book.title} does not exist!")

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

    def remove_member(self, member):
        for m in self.members:
            if m.id == member.id:
                self.members.remove(m)
                print(f"{m.name} was deleted.")
                return
        print(f"{member.name} not found!")

    def list_members(self):
        if not self.members:
            print("There is no member yet...")
        for member in self.members:
            print(member)

    def borrow_book(self, member, book):
        # check member
        if member not in self.members:
            raise ValueError(f"{member.name} has not registered yet!")

        # find the actual book
        if book not in self.books:
            raise ValueError(f"{book.title} does not exist!")

        # check availability
        if not book.available:
            raise ValueError(f"{book.title} is not available...")

        # borrow action
        book.available = False
        member.borrowed_books.append(book)
        print(f"{book.title} was borrowed by {member.name}.")

    def return_book(self, member, book):
        # check member
        if member not in self.members:
            raise ValueError(f"{member.name} has not registered yet!")

        # find the actual book
        if book not in self.books:
            raise ValueError(f"{book.title} does not exist!")

        # check availability
        if book.available:
            raise ValueError(f"{book.title} is already available!")

        if book not in member.borrowed_books:
            raise ValueError(f"{member.name} has not borrowed this {book.title}!")

        # return action
        book.available = True
        member.borrowed_books.remove(book)
        print(f"{book.title} was returned by {member.name}")

    def save_state(self):
        with open(self.filename, "w") as f:
            f.write("BOOKS:\n")
            for book in self.books:
                f.write(f"{book.title}|{book.author}|{book.available}\n")

            f.write("MEMBERS:\n")
            for member in self.members:
                # titles = ",".join(book.title for book in member.borrowed_books)
                f.write(f"{member.name}|{member.id}|{titles}\n")


    



#  save and load file....
# RCR -> call nima
# study RF
# study Proba
# study PA on paper
# study image


if __name__ == "__main__":
    book1 = Book("book 1", "author 1")
    book2 = Book("book 2", "author 2")
    book3 = Book("book 3", "author 3")  # defined but not added to lib
    # fake_book1 = Book("book 1", "author 1")  # same title, different object

    member1 = Member("member 1", 1, None)
    member2 = Member("member 2", 2, None)
    member3 = Member("member 3", 3, None)  # not added as a member

    lib = Library()
    lib.add_book(book1)
    lib.add_book(book2)
    # lib.list_books()
    lib.add_member(member1)
    lib.add_member(member2)
    lib.list_members()

    lib.borrow_book(member1, book1)  # book 1 was borrowed by member 1.
    lib.borrow_book(member1, book2)
    # lib.borrow_book(member1,fake_book1)

    # lib.return_book(member1, book1)
    lib.save_state()
    # lib.load_state()
    # lib.list_books()
    # lib.list_members()
    # # lib.remove_member(member1)
    # # lib.remove_member(member2)
    # # lib.list_members()

    print()
