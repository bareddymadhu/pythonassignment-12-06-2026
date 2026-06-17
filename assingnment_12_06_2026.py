set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1.add(9)
print("adding an element:", set1)
set1.remove(2)
print("removing an element:", set1)


print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference :", set1 - set2)

# Book catalog functions
books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction", "year": 1988},
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-help", "year": 2018},
    {"title": "Clean Code", "author": "Robert C. Martin", "genre": "Programming", "year": 2008},
]
def add_book(catalog, title, author, genre, year):
    catalog.append({"title": title, "author": author, "genre": genre, "year": year})
    return catalog
def remove_book(catalog, title):
    for book in catalog:
        if book["title"].lower() == title.lower():
            catalog.remove(book)
            return True
    return False
def search_books(catalog, title=None, author=None, genre=None):
    results = []
    for book in catalog:
        if title and title.lower() not in book["title"].lower():
            continue
        if author and author.lower() not in book["author"].lower():
            continue
        if genre and genre.lower() not in book["genre"].lower():
            continue
        results.append(book)
    return results
def display_books(catalog, sort_by="title"):
    return sorted(
        catalog,
        key=lambda book: book[sort_by].lower() if isinstance(book[sort_by], str) else book[sort_by],
    )      
# Example usage
add_book(books, "The Pragmatic Programmer", "Andrew Hunt", "Programming", 1999)
print("Books after adding a new book:", display_books(books))
#remove a book
remove_book(books, "Atomic Habits")

print("Books after removing 'Atomic Habits':", display_books(books))  
#search for books by author      
search_results = search_books(books, author="Robert C. Martin")
print("Search results for author 'Robert C. Martin':", search_results)      
# Display books sorted by year
print("Books sorted by year:", display_books(books, sort_by="year"))
