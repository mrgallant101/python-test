
class Library:
    shelves = {}

    @classmethod
    def view_all_books(cls):
        print("These are all the books and their respective ratings\n", Library.shelves)

    @classmethod
    def add_book(cls):
        response = True
        while response:
            book_name = input("Enter the name of the book: ")
            book_rating = float(input("Enter the ratings of the book: "))

            new_library = {
                book_name: {
                    "book name": book_name,
                    "book ranking": book_rating,
                },

             }

            cls.shelves.update(new_library)

            response = input("Do you want to enter another book? Type 'Yes' or 'No': ").lower()
            if book_name in cls.shelves[book_name].keys():
                print("Book already exist")
                break
            elif response == "no":
                break

            else:
                continue

    @classmethod
    def get_book_by_name(cls):
        book_name = input("Enter the name of book you want to view details: ")
        if book_name in cls.shelves.keys():
            print(f" The details of the book {book_name} is {cls.shelves[book_name]}")
        else:
            print(f"The book {book_name} does not exist")

    @classmethod
    def update_ratings(cls):
        book_name = input("Enter the name of the book you want to update its ratings: ")
        new_rating = float(input("Enter new ratings: "))
        if book_name in cls.shelves.keys():
            cls.shelves[book_name] = new_rating
            print(f"The new ratings of {book_name} is {new_rating}")
        else:
            print(f"The book {book_name} does not exist")

    @classmethod
    def delete_book(cls):
        is_enough = True
        while is_enough:
            book_name = input("Enter the name of the book you want to delete: ")
            del cls.shelves[book_name]
            print(f"{book_name} has being deleted successfully")
            response = input("Do you want to delete another book? type 'Yes' or 'no' ").lower()
            if response == "yes":
                continue
            else:
                break


lib = Library()
lib.add_book()
lib.view_all_books()
lib.get_book_by_name()
lib.view_all_books()
lib.update_ratings()
lib.view_all_books()
lib.delete_book()
lib.view_all_books()








