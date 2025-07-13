# CREATE Operation

## Command:
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
```

## Expected Output:
```
# The book instance is created and saved to the database
# No output is displayed, but the book is successfully stored
```

## Verification:
```python
print(f"Book created: {book.title} by {book.author} ({book.publication_year})")
```

## Expected Verification Output:
```
Book created: 1984 by George Orwell (1949)
``` 