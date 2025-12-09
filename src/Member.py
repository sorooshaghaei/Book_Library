class Member:
    def __init__(self, name, id, borrowed_books):
        self.name = name
        self.id = id
        self.borrowed_books = borrowed_books

    def __str__(self):
        return f"member name is {self.name} with id: {self.id} and borrowed books are: {self.borrowed_books}"


if __name__ == "__main__":
    member1 = Member("ali", 1, 0)
    print(member1)
