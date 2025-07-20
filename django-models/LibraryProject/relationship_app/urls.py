from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view for listing all books
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view for library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
] 