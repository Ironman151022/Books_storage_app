import utilities.database as db

menu_card = """
Enter:
- 'a' for adding a book
- 'l' for listing a book
- 'd' for deleting a book
- 'f' for searching a book
- 'r' for marking book as read
- 'q' for quiting: """

def prompt_add():
    name = input("Enter book name: ").lower()
    author = input("Enter author of book: ").lower()
    books = db.print_info()
    for book in books :
        if name == book['book']:
            print('Book already exist -_-')
            break
    else:
        db.add_book(name,author)

def listing():
        db.listing()

def search():
    name = input("Enter name of the book to be searched: ").lower()
    db.searching(name)

def delete_book():
    name = input("Enter name of book to be deleted: ").lower()
    db.deleting(name)
def marking():
    name = input('Enter the name of the book to be marked as read: ').lower()
    db.mark(name)






user_options={
    'a' : prompt_add,
    'l' : listing,
    'f' : search,
    'd' : delete_book,
    'r' : marking,
    'smash': db._smash
}
def menu():
    db.create_database()
    u = input(menu_card).lower()

    while u!='q':
        if u in user_options:
            selection = user_options[u]
            selection()

        else:
            print("Enter a valid key -_-")
        u = input(menu_card).lower()

menu()