from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book, Author, Librarian
from .models import Library

# Create your views here.

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
