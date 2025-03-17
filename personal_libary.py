import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []


def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)



def add_book(library):
    title = input("Enter the title of the Book ").strip().lower()
    author = input("Enter the author of the book:").strip().lower()
    year = input("Enter the year of book:").strip().lower()
    genre = input("Enter the genre of book:").strip().lower()
    read = input("Have you read the book? (yes/no)").lower() == 'yes'

    new_book = {
        "title": title,
        "author": author,
        "year"  : year, 
        "genre" : genre,
        "read"  :  read
    }
     
    library.append(new_book)
    save_library(library)
    print(f"Book {title} added successfully")

def remove_book(library):
    title = input("Enter the title book to remove from the library:").strip().lower()

    found = False
    for book in library:
        if book["title"].strip().lower() == title:
            library.remove(book)
            found = True
            break
    if found:
        save_library(library)
        print(f"Book {title} removed successfully")
    else:
        print(f"Book {title.title()} not found")
    
           
           
           
def search_books(library):
    search = input("search for book by title or author:").strip().lower()
    if search not in ["title", "author"]:
        print("Invalid search term. Please try again")
        return
    search_term = input(f"Enter {search} to search: ").strip().lower()
    results = [book for book in library if search in book and search_term in book[search].strip().lower()]
    
    
     
    if results:
        for book in results:
            status = "read" if book["read"] else "not read"
            print(f"{book['title']} by {book['author']} - {book['year']}- {book['genre']}- {status}")
    else:
        print(f"No books found for '{search_term}' in {search}.")

def display_all_books(library):
    if library:
        for book in library:
            status = "read" if book["read"] else "not read"
            print(f"{book['title']} by {book['author']} - {book['year']}- {book['genre']}- {status}")
    else:
         print("No books in the laibry")


     
def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book["read"]])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    print(f"Total books: {total_books}")
    print(f"Total read books: {read_books}")
    print(f"percentage read: {percentage_read:.2f}%")


def main():
    library = load_library()
    while True:
        
        print("\n📚 Personal Library Menu")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search books")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Quit")

        choice = input("Enter your choice:").strip()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4": 
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again")
if __name__ == "__main__":
    main()


