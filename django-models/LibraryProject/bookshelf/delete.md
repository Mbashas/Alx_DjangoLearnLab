# DELETE Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
```

## Expected Output:
```
(1, {'bookshelf.Book': 1})
```

## Verification:
```python
# Try to retrieve all books to confirm deletion
all_books = Book.objects.all()
print(f"Number of books in database: {all_books.count()}")
```

## Expected Verification Output:
```
Number of books in database: 0
```

## Alternative Delete Command:
```python
# Delete using filter and delete methods
Book.objects.filter(title="Nineteen Eighty-Four").delete()
```

## Alternative Expected Output:
```
(1, {'bookshelf.Book': 1})
``` 