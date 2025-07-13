# UPDATE Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```

## Expected Output:
```
# No output is displayed, but the book title is updated in the database
```

## Verification:
```python
updated_book = Book.objects.get(author="George Orwell")
print(f"Updated title: {updated_book.title}")
```

## Expected Verification Output:
```
Updated title: Nineteen Eighty-Four
```

## Alternative Update Command:
```python
# Update using update() method
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")
``` 