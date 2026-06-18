def set_operations():
    # Initial list of numbers
    numbers = [1, 2, 3, 4, 5, 3, 2, 6]
    unique_numbers = set(numbers)
    print("Initial unique set:", unique_numbers)

    # Add new elements
    unique_numbers.add(7)
    unique_numbers.update([8, 9])
    print("After adding elements:", unique_numbers)

    # Remove elements
    unique_numbers.discard(2)   # discard won't raise error if not found
    unique_numbers.remove(3)    # remove will raise error if not found
    print("After removing elements:", unique_numbers)

    # Another set for operations
    other_set = {5, 6, 7, 10}

    # Union
    print("Union:", unique_numbers.union(other_set))

    # Intersection
    print("Intersection:", unique_numbers.intersection(other_set))

    # Difference
    print("Difference:", unique_numbers.difference(other_set))


# -------------------------------
# Part 2: Dictionary-based Library System
# -------------------------------

class Library:
    def __init__(self):
        self.books = {}  # key = title, value = dict with details

    def add_book(self, title, author, year, genre):
        self.books[title] = {
            "author": author,
            "year": year,
            "genre": genre
        }
        print(f"Book '{title}' added.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"Book '{title}' removed.")
        else:
            print(f"Book '{title}' not found.")

    def search_books(self, keyword, by="title"):
        results = []
        for title, details in self.books.items():
            if by == "title" and keyword.lower() in title.lower():
                results.append((title, details))
            elif by == "author" and keyword.lower() in details["author"].lower():
                results.append((title, details))
            elif by == "genre" and keyword.lower() in details["genre"].lower():
                results.append((title, details))
        return results

    def display_books(self, sort_by="title"):
        sorted_books = sorted(self.books.items(), key=lambda x: x[0] if sort_by=="title" else x[1]["author"])
        for title, details in sorted_books:
            print(f"{title} - {details['author']} ({details['year']}) [{details['genre']}]")

# -------------------------------
# Testing Implementation
# -------------------------------

if __name__ == "__main__":
    # Test set operations
    print("=== Set Operations ===")
    set_operations()

    # Test library system
    print("\n=== Library System ===")
    library = Library()
    library.add_book("1984", "George Orwell", 1949, "Dystopian")
    library.add_book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")

    print("\nAll books sorted by title:")
    library.display_books(sort_by="title")

    print("\nSearch by author 'George Orwell':")
    print(library.search_books("George Orwell", by="author"))

    library.remove_book("1984")

    print("\nAll books sorted by author:")
    library.display_books(sort_by="author")
