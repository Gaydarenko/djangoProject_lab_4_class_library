from django.urls import path
from .views import LibraryView, CreateView, AuthorsView, CreateFormView, SearchView, BookFormView, BooksView, BookView

urlpatterns = [
    path('', LibraryView.as_view()),
    path('create/', CreateView.as_view(), name='create'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('create-form/', CreateFormView.as_view(), name='create-form'),
    path('search/', SearchView.as_view(), name='search'),
    path('create_book/', BookFormView.as_view(), name='create-book'),
    path('books/', BooksView.as_view(), name='books'),
    path('books/<int:page>', BooksView.as_view()),
    path('book/', BookView.as_view(), name='book'),
]
