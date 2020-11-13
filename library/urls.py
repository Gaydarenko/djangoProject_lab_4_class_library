from django.urls import path
from .views import LibraryView, CreateAuthorView, AuthorsListView, CreateAuthorFormView, SearchView, CreateBookFormView, BooksListView, BookView, AuthorView

urlpatterns = [
    path('', LibraryView.as_view()),
    path('create/', CreateAuthorView.as_view(), name='create'),
    path('authors/', AuthorsListView.as_view(), name='authors'),
    path('authors/<int:page>', AuthorsListView.as_view()),
    path('author/', AuthorView.as_view(), name='author'),
    path('author/<int:id>', AuthorView.as_view()),
    path('create-form/', CreateAuthorFormView.as_view(), name='create-form'),
    path('search/', SearchView.as_view(), name='search'),
    path('create_book/', CreateBookFormView.as_view(), name='create-book'),
    path('books/', BooksListView.as_view(), name='books'),
    path('books/<int:page>', BooksListView.as_view()),
    path('book/', BookView.as_view(), name='book'),
    path('book/<int:id>', BookView.as_view()),
]
