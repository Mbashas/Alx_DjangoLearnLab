# CRUD Operations Documentation

This document contains all the CRUD (Create, Read, Update, Delete) operations performed on the Book model in the Django shell.

## Model Definition

The Book model is defined in `bookshelf/models.py`:

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return self.title
```

## CRUD Operations

### 1. CREATE Operation

**Command:**
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(f"Book created: {book.title} by {book.author} ({book.publication_year})")
```

**Expected Output:**
```
Book created: 1984 by George Orwell (1949)
```

### 2. RETRIEVE Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

**Expected Output:**
```
Title: 1984
Author: George Orwell
Publication Year: 1949
```

### 3. UPDATE Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(author="George Orwell")
print(f"Updated title: {updated_book.title}")
```

**Expected Output:**
```
Updated title: Nineteen Eighty-Four
```

### 4. DELETE Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
delete_result = book.delete()
print(f"Delete result: {delete_result}")
all_books = Book.objects.all()
print(f"Number of books in database: {all_books.count()}")
```

**Expected Output:**
```
Delete result: (1, {'bookshelf.Book': 1})
Number of books in database: 0
```

## Summary

These operations demonstrate the basic CRUD functionality of Django's ORM:
- **Create**: Use `Model()` constructor and `save()` method
- **Read**: Use `Model.objects.get()` or `Model.objects.all()`
- **Update**: Modify instance attributes and call `save()`
- **Delete**: Call `delete()` method on instance or queryset

All operations were successfully performed on the Book model with the specified attributes. 