"""
Sample queries demonstrating Django ORM relationships.

This script contains sample queries for the relationship_app models:
- Author (ForeignKey relationship with Book)
- Book (ForeignKey to Author, ManyToMany with Library)
- Library (ManyToMany with Book, OneToOne with Librarian)
- Librarian (OneToOne with Library)

To run these queries in Django shell:
python manage.py shell
exec(open('relationship_app/query_samples.py').read())
"""

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author():
    """
    Query all books by a specific author.
    Demonstrates ForeignKey relationship (Author -> Book)
    """
    try:
        # Get an author (assuming we have some data)
        author_name = "J.K. Rowling"  # Example author
        author = Author.objects.get(name=author_name)
        
        # Query all books by this author using the ForeignKey relationship
        books_by_author = Book.objects.filter(author=author)
        
        print(f"\nBooks by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
            
        # Alternative approach using the reverse relationship
        books_by_author_reverse = author.books.all()
        print(f"\nUsing reverse relationship - Books by {author_name}:")
        for book in books_by_author_reverse:
            print(f"- {book.title}")
            
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found. Please create some sample data first.")

def query_all_books_in_library():
    """
    List all books in a library.
    Demonstrates ManyToMany relationship (Library -> Book)
    """
    try:
        # Get a library (assuming we have some data)
        library_name = "Central Library"  # Example library
        library = Library.objects.get(name=library_name)
        
        # Query all books in this library using the ManyToMany relationship
        books_in_library = library.books.all()
        
        print(f"\nBooks in {library_name}:")
        for book in books_in_library:
            print(f"- {book.title} by {book.author.name}")
            
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found. Please create some sample data first.")

def query_librarian_for_library():
    """
    Retrieve the librarian for a library.
    Demonstrates OneToOne relationship (Library -> Librarian)
    """
    try:
        # Get a library (assuming we have some data)
        library_name = "Central Library"  # Example library
        library = Library.objects.get(name=library_name)
        
        # Query the librarian for this library using the OneToOne relationship
        librarian = library.librarian
        
        print(f"\nLibrarian for {library_name}:")
        print(f"- {librarian.name}")
        
        # Alternative approach using the Librarian model
        librarian_alt = Librarian.objects.get(library=library)
        print(f"Alternative query - Librarian: {librarian_alt.name}")
        
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found. Please create some sample data first.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")

def create_sample_data():
    """
    Create sample data to demonstrate the queries.
    """
    print("Creating sample data...")
    
    # Create authors
    author1 = Author.objects.get_or_create(name="J.K. Rowling")[0]
    author2 = Author.objects.get_or_create(name="George Orwell")[0]
    author3 = Author.objects.get_or_create(name="Harper Lee")[0]
    
    # Create books
    book1 = Book.objects.get_or_create(
        title="Harry Potter and the Philosopher's Stone", 
        author=author1
    )[0]
    book2 = Book.objects.get_or_create(
        title="Harry Potter and the Chamber of Secrets", 
        author=author1
    )[0]
    book3 = Book.objects.get_or_create(
        title="1984", 
        author=author2
    )[0]
    book4 = Book.objects.get_or_create(
        title="Animal Farm", 
        author=author2
    )[0]
    book5 = Book.objects.get_or_create(
        title="To Kill a Mockingbird", 
        author=author3
    )[0]
    
    # Create libraries
    library1 = Library.objects.get_or_create(name="Central Library")[0]
    library2 = Library.objects.get_or_create(name="University Library")[0]
    
    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2, book3, book5)
    library2.books.add(book3, book4, book5)
    
    # Create librarians
    librarian1 = Librarian.objects.get_or_create(
        name="Alice Johnson", 
        library=library1
    )[0]
    librarian2 = Librarian.objects.get_or_create(
        name="Bob Smith", 
        library=library2
    )[0]
    
    print("Sample data created successfully!")

def run_all_queries():
    """
    Run all sample queries.
    """
    print("=== Django ORM Relationship Queries ===")
    
    # Create sample data first
    create_sample_data()
    
    # Run the queries
    query_all_books_by_author()
    query_all_books_in_library()
    query_librarian_for_library()

# Uncomment the line below to run all queries when script is executed
# run_all_queries()

print("Query samples loaded. You can run individual functions or call run_all_queries() to execute all samples.") 