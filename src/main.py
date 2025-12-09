
# class Book:
#     """
#     Modélisation d'un livre (Partie 1.1)
#     """
#     def __init__(self, title, author, available=True):
#         self.title = title
#         self.author = author
#         self.available = available  # boolean

#     def __str__(self):
#         status = "Disponible" if self.available else "Emprunté"
#         return f"'{self.title}' par {self.author} ({status})"

# class Member:
#     """
#     Modélisation d'un adhérent (Partie 1.2)
#     """
#     def __init__(self, name, member_id):
#         self.name = name
#         self.member_id = member_id
#         self.borrowed_books = []  # List of Book objects

#     def __str__(self):
#         # Affichage sur la sortie standard
#         books_str = ", ".join([b.title for b in self.borrowed_books])
#         return f"ID: {self.member_id} | Nom: {self.name} | Emprunts: [{books_str}]"

# class Library:
#     """
#     Gestion de la bibliothèque (Partie 1.3)
#     """
#     def __init__(self):
#         self.books = []      # List of Book objects
#         self.members = []    # List of Member objects
#         self.filename = "libstate"

#         # Chargement automatique au démarrage (Partie 2.2)
#         self.load_state()

#     # --- Gestion des Livres ---
#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Livre ajouté: {book.title}")

#     def remove_book(self, book_title):
#         for i, book in enumerate(self.books):
#             if book.title == book_title:
#                 if not book.available:
#                     print("Impossible de supprimer: le livre est actuellement emprunté.")
#                     return
#                 del self.books[i]
#                 print(f"Livre supprimé: {book_title}")
#                 return
#         # Gestion de l'exception (Partie 1.3)
#         print(f"Erreur: Le livre '{book_title}' n'est pas dans la bibliothèque.")

#     def list_books(self):
#         print("--- Liste des Livres ---")
#         if not self.books:
#             print("Aucun livre.")
#         for b in self.books:
#             print(b)

#     # --- Gestion des Membres ---
#     def add_member(self, member):
#         # Check for duplicate ID
#         for m in self.members:
#             if m.member_id == member.member_id:
#                 print(f"Erreur: L'ID {member.member_id} existe déjà.")
#                 return
#         self.members.append(member)
#         print(f"Membre ajouté: {member.name}")

#     def remove_member(self, member_id):
#         for i, member in enumerate(self.members):
#             if member.member_id == member_id:
#                 if len(member.borrowed_books) > 0:
#                     print("Impossible de supprimer: ce membre a des livres à rendre.")
#                     return
#                 del self.members[i]
#                 print(f"Membre supprimé: {member_id}")
#                 return
#         # Gestion de l'exception (Partie 1.3)
#         print(f"Erreur: Le membre ID {member_id} n'existe pas.")

#     def list_members(self):
#         print("--- Liste des Adhérents ---")
#         if not self.members:
#             print("Aucun membre.")
#         for m in self.members:
#             print(m)

#     # --- Emprunts (Partie 1.4) ---
#     def borrow_book(self, member_id, book_title):
#         # Find member
#         member = None
#         for m in self.members:
#             if m.member_id == member_id:
#                 member = m
#                 break
#         if not member:
#             print("Membre introuvable.")
#             return

#         # Find book
#         book = None
#         for b in self.books:
#             if b.title == book_title:
#                 book = b
#                 break
#         if not book:
#             print("Livre introuvable.")
#             return

#         if not book.available:
#             print(f"Le livre '{book_title}' n'est pas disponible.")
#         else:
#             book.available = False
#             member.borrowed_books.append(book)
#             print(f"'{book_title}' emprunté par {member.name}.")

#     def return_book(self, member_id, book_title):
#         member = None
#         for m in self.members:
#             if m.member_id == member_id:
#                 member = m
#                 break
#         if not member:
#             print("Membre introuvable.")
#             return

#         for i, book in enumerate(member.borrowed_books):
#             if book.title == book_title:
#                 book.available = True
#                 del member.borrowed_books[i]
#                 print(f"'{book_title}' rendu par {member.name}.")
#                 return

#         print(f"Ce membre n'a pas emprunté le livre '{book_title}'.")

#     # --- Sauvegarde et Chargement (Partie 2) ---
#     def save_state(self):
#         """
#         Format de sauvegarde personnalisé (sans import json/pickle):
#         B|Titre|Auteur|Disponibilité
#         M|Nom|ID|Livre1;Livre2;Livre3
#         """
#         try:
#             f = open(self.filename, "w")

#             # Sauvegarde des livres
#             for b in self.books:
#                 # 1 if True else 0
#                 avail = "1" if b.available else "0"
#                 line = f"B|{b.title}|{b.author}|{avail}\n"
#                 f.write(line)

#             # Sauvegarde des membres
#             for m in self.members:
#                 borrowed_titles = ";".join([b.title for b in m.borrowed_books])
#                 line = f"M|{m.name}|{m.member_id}|{borrowed_titles}\n"
#                 f.write(line)

#             f.close()
#             print("État sauvegardé dans 'libstate'.")
#         except:
#             print("Erreur lors de la sauvegarde.")

#     def load_state(self):
#         try:
#             # Check if file exists by trying to open it in read mode
#             try:
#                 f = open(self.filename, "r")
#             except:
#                 # File doesn't exist yet, simple return
#                 return

#             content = f.read().splitlines()
#             f.close()

#             self.books = []
#             self.members = []

#             # First pass: Load all books
#             for line in content:
#                 parts = line.split("|")
#                 if parts[0] == "B":
#                     title = parts[1]
#                     author = parts[2]
#                     avail = True if parts[3] == "1" else False
#                     new_book = Book(title, author, avail)
#                     self.books.append(new_book)

#             # Second pass: Load members and link borrowed books
#             for line in content:
#                 parts = line.split("|")
#                 if parts[0] == "M":
#                     name = parts[1]
#                     mid = parts[2]
#                     borrowed_str = parts[3]

#                     new_member = Member(name, mid)

#                     # Relink borrowed books by title
#                     if borrowed_str:
#                         titles = borrowed_str.split(";")
#                         for t in titles:
#                             # Find the book object in self.books
#                             for b in self.books:
#                                 if b.title == t:
#                                     new_member.borrowed_books.append(b)
#                                     # Ensure consistency if file was messed up
#                                     b.available = False
#                                     break

#                     self.members.append(new_member)

#             print(f"Données chargées : {len(self.books)} livres, {len(self.members)} membres.")

#         except Exception as e:
#             print(f"Erreur lors du chargement : {e}")

# # --- Interface (Partie 2.3) ---
# def main():
#     lib = Library()

#     while True:
#         print("\n=== GESTION BIBLIOTHEQUE ===")
#         print("1. Ajouter un livre")
#         print("2. Supprimer un livre")
#         print("3. Lister les livres")
#         print("4. Ajouter un membre")
#         print("5. Supprimer un membre")
#         print("6. Lister les membres")
#         print("7. Emprunter un livre")
#         print("8. Rendre un livre")
#         print("9. Sauvegarder et Quitter")

#         choice = input("Choix: ")

#         if choice == "1":
#             t = input("Titre: ")
#             a = input("Auteur: ")
#             lib.add_book(Book(t, a))
#         elif choice == "2":
#             t = input("Titre du livre à supprimer: ")
#             lib.remove_book(t)
#         elif choice == "3":
#             lib.list_books()
#         elif choice == "4":
#             n = input("Nom: ")
#             i = input("ID Unique: ")
#             lib.add_member(Member(n, i))
#         elif choice == "5":
#             i = input("ID du membre à supprimer: ")
#             lib.remove_member(i)
#         elif choice == "6":
#             lib.list_members()
#         elif choice == "7":
#             mid = input("ID Membre: ")
#             bt = input("Titre Livre: ")
#             lib.borrow_book(mid, bt)
#         elif choice == "8":
#             mid = input("ID Membre: ")
#             bt = input("Titre Livre: ")
#             lib.return_book(mid, bt)
#         elif choice == "9":
#             lib.save_state()
#             print("Au revoir!")
#             break
#         else:
#             print("Choix invalide.")

# if __name__ == "__main__":
#     main()
