class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title}|{self.author}|{self.available}"


class Member:
    def __init__(self, name, id, borrowed_books=None):
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

        self.load_state()

    def add_book(self, book):
        for b in self.books:
            if b.title == book.title:
                print(f"{b.title} by author:{b.author} already exists.")
                return
        self.books.append(book)
        print(f"{book.title} was added.")

    def remove_book(self, book_title):
        for b in self.books:
            if b.title == book_title:
                if b.available:
                    self.books.remove(b)
                    print(f"{b.title} was removed.")
                    return
                else:
                    print(f"{b.title} is borrowed by someone.")
                    return
        print(f"{book_title} does not exist!")

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

    def remove_member(self, member_id):
        for m in self.members:
            if m.id == member_id:
                self.members.remove(m)
                print(f"{m.name} with id {m.id} was deleted.")
                return
        print(f"id: {member_id} does not belong to anyone!")

    def list_members(self):
        if not self.members:
            print("There is no member yet...")
        for member in self.members:
            print(member)

    def find_member_by_id(self, member_ID: int):
        for member in self.members:
            if member.id == member_ID:
                return member
        raise ValueError("Member not found!")

    def find_book_by_title(self, book_title):
        for book in self.books:
            if book.title == book_title:
                return book
        raise ValueError("Book not found!")

    def borrow_book(self, member_id, book_title):
        # find book and member
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_title(book_title)

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
                titles = []
                for book in member.borrowed_books:
                    titles.append(book.title)
                titles = ",".join(titles)
                f.write(f"{member.name}|{member.id}|{titles}\n")

    def load_state(self):
        self.books = []
        self.members = []
        pointer = ""
        try:
            with open(self.filename) as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("could not find the saved file!")
            return

        for line in lines:
            line = line.strip()
            if line == "BOOKS:":
                pointer = "books"
                continue
            if line == "MEMBERS:":
                pointer = "members"
                continue

            if pointer == "books":
                title, author, available = line.split("|")
                if available == "True":
                    available = True
                elif available == "False":
                    available = False

                new_book = Book(title, author, available)
                self.books.append(new_book)

            if pointer == "members":
                name, id, borrowed_titles = line.split("|")
                id = int(id)
                borrowed_books = []

                if borrowed_titles:
                    titles = borrowed_titles.split(",")
                    for title in titles:
                        for book in self.books:
                            if title == book.title:
                                borrowed_books.append(book)
                                book.available = False

                new_member = Member(name, id, borrowed_books)
                self.members.append(new_member)


if __name__ == "__main__":
    lib = Library()
    print("\n===  Welcome to Library...  ===")
    while True:
        try:
            print("1. Add a book")
            print("2. Remove a book")
            print("3. List of books")
            print("4. Add a member")
            print("5. Remove a member")
            print("6. list members")
            print("7. Borrow a book by a member")
            print("8. Return a book by a member")
            print("9. Save and quit")
            print("10. Discard changes and quit")

            choice = int(input("Choose from 1 to 10: "))

            if choice == 1:
                title = input("Enter the title of book you want to add: ")
                author = input("Enter the name of author: ")
                lib.add_book(Book(title, author))

            elif choice == 2:
                title = input("Enter the title of book you want to remove: ")
                sure = input("Are you sure? (answer with yes or no) ")
                try:
                    if sure == "yes":
                        lib.remove_book(title)
                    elif sure == "no":
                        print("It was not deleted.")
                    else:
                        print("wrong input")
                except ValueError as e:
                    print(e)

            elif choice == 3:
                lib.list_books()
            elif choice == 4:
                name = input("Enter the name of member you want to add: ")
                id = int(input("What is she/he id number? "))
                lib.add_member(Member(name, id))
            elif choice == 5:
                member_id = int(input("Enter the id of member you want to remove: "))
                yes_or_no = input(f"Deleting {member_id}?(answer with yes or no) ")
                try:
                    if yes_or_no == "yes":
                        lib.remove_member(member_id)
                    elif yes_or_no == "no":
                        print("It was not deleted.")
                    else:
                        print("wrong input.")
                except ValueError as e:
                    print(e)

            elif choice == 6:
                lib.list_members()

            elif choice == 7:
                member_id = int(input("Enter member ID: "))
                book_title = input("Enter book title: ")
                lib.borrow_book(member_id, book_title)

            elif choice == 8:
                pass
            elif choice == 9:
                lib.save_state()
                print("Bye...")
                break
            elif choice == 10:
                print("Changes were not saved")
                break
            else:
                print("choose a correct number from 1 to 9!!!!")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
