from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib import messages
from django import forms
from .models import Book, Author, Librarian, UserProfile
from .models import Library

# Create your views here.

# Book Form for creating and editing books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

def list_books(request):
    """
    Function-based view that lists all books stored in the database.
    Renders a list of book titles and their authors.
    """
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library,
    listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context if needed
        context['books_count'] = self.object.books.count()
        return context

# Authentication Views

def register(request):
    """
    User registration view using Django's built-in UserCreationForm.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app:list_books')  # Redirect after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class CustomLoginView(LoginView):
    """
    Custom login view using Django's built-in LoginView.
    """
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return '/relationship/books/'  # Redirect to books list after login

class CustomLogoutView(LogoutView):
    """
    Custom logout view using Django's built-in LogoutView.
    """
    template_name = 'relationship_app/logout.html'

# Role-Based Access Control Views

def is_admin(user):
    """
    Check if user has Admin role.
    """
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """
    Check if user has Librarian role.
    """
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """
    Check if user has Member role.
    """
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    """
    Admin view accessible only to users with Admin role.
    """
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    """
    Librarian view accessible only to users with Librarian role.
    """
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    """
    Member view accessible only to users with Member role.
    """
    return render(request, 'relationship_app/member_view.html')

# Permission-Required Views for Book Operations

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """
    View for adding a new book. Requires 'can_add_book' permission.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" has been added successfully!')
            return redirect('relationship_app:list_books')
    else:
        form = BookForm()
    
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    """
    View for editing an existing book. Requires 'can_change_book' permission.
    """
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" has been updated successfully!')
            return redirect('relationship_app:list_books')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """
    View for deleting a book. Requires 'can_delete_book' permission.
    """
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book_title = book.title
        book.delete()
        messages.success(request, f'Book "{book_title}" has been deleted successfully!')
        return redirect('relationship_app:list_books')
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})
