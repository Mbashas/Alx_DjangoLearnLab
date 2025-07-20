# Django Models - Advanced Model Relationships

This project demonstrates Django's ORM capabilities by implementing complex model relationships using ForeignKey, ManyToMany, and OneToOne fields.

## Project Structure

```
django-models/
├── LibraryProject/
│   ├── relationship_app/
│   │   ├── models.py          # Complex models with relationships
│   │   ├── query_samples.py   # Sample queries demonstrating relationships
│   │   └── ...
│   ├── LibraryProject/
│   │   ├── settings.py        # Project settings
│   │   └── ...
│   └── manage.py
└── README.md
```

## Models Overview

### Author Model
- **Fields**: `name` (CharField)
- **Relationships**: One-to-Many with Book (ForeignKey reverse relationship)

### Book Model  
- **Fields**: `title` (CharField), `author` (ForeignKey to Author)
- **Relationships**: 
  - Many-to-One with Author (ForeignKey)
  - Many-to-Many with Library

### Library Model
- **Fields**: `name` (CharField), `books` (ManyToManyField to Book)
- **Relationships**: 
  - Many-to-Many with Book
  - One-to-One with Librarian

### Librarian Model
- **Fields**: `name` (CharField), `library` (OneToOneField to Library)
- **Relationships**: One-to-One with Library

## Relationship Types Demonstrated

1. **ForeignKey (One-to-Many)**: Author → Book
   - One author can have multiple books
   - Each book belongs to one author

2. **ManyToManyField (Many-to-Many)**: Library ↔ Book
   - One library can have multiple books
   - One book can be in multiple libraries

3. **OneToOneField (One-to-One)**: Library ↔ Librarian
   - Each library has exactly one librarian
   - Each librarian manages exactly one library

## Setup Instructions

1. **Navigate to project directory:**
   ```bash
   cd django-models/LibraryProject
   ```

2. **Install dependencies:**
   ```bash
   pip install django
   ```

3. **Apply migrations:**
   ```bash
   python manage.py makemigrations relationship_app
   python manage.py migrate
   ```

## Usage

### Running Sample Queries

1. **Open Django shell:**
   ```bash
   python manage.py shell
   ```

2. **Load and run sample queries:**
   ```python
   exec(open('relationship_app/query_samples.py').read())
   run_all_queries()
   ```

### Individual Query Functions

The `query_samples.py` file contains the following functions:

- `query_all_books_by_author()` - Demonstrates ForeignKey relationship
- `query_all_books_in_library()` - Demonstrates ManyToMany relationship  
- `query_librarian_for_library()` - Demonstrates OneToOne relationship
- `create_sample_data()` - Creates test data for demonstrations
- `run_all_queries()` - Executes all sample queries

### Sample Query Results

When you run the queries, you'll see output like:

```
=== Django ORM Relationship Queries ===
Creating sample data...
Sample data created successfully!

Books by J.K. Rowling:
- Harry Potter and the Philosopher's Stone
- Harry Potter and the Chamber of Secrets

Books in Central Library:
- Harry Potter and the Philosopher's Stone by J.K. Rowling
- Harry Potter and the Chamber of Secrets by J.K. Rowling
- 1984 by George Orwell
- To Kill a Mockingbird by Harper Lee

Librarian for Central Library:
- Alice Johnson
```

## Key Learning Points

1. **ForeignKey**: Creates a many-to-one relationship with `on_delete` parameter
2. **ManyToManyField**: Creates a many-to-many relationship with automatic intermediate table
3. **OneToOneField**: Creates a one-to-one relationship, similar to ForeignKey with unique=True
4. **Related Names**: Use `related_name` parameter for reverse relationships
5. **Query Patterns**: Different ways to query across relationships using Django ORM

## Advanced Features

- **Reverse Relationships**: Access related objects using `related_name`
- **Cross-table Queries**: Filter and query across multiple related models
- **Efficient Queries**: Use `select_related()` and `prefetch_related()` for optimization

This project serves as a comprehensive example of implementing and querying complex model relationships in Django. 