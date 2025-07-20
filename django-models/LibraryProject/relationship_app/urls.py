from django.urls import path
from . import views
from .views import list_books, register, CustomLoginView, CustomLogoutView

app_name = 'relationship_app'

urlpatterns = [
    # Function-based view for listing all books
    path('books/', list_books, name='list_books'),
    
    # Class-based view for library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
] 