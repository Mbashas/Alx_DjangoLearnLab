# RETRIEVE Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

## Expected Output:
```
Title: 1984
Author: George Orwell
Publication Year: 1949
```

## Alternative Retrieve Command:
```python
# Retrieve all books
all_books = Book.objects.all()
for book in all_books:
    print(f"{book.title} by {book.author} ({book.publication_year})")
```

## Expected Alternative Output:
```
1984 by George Orwell (1949)
``` 