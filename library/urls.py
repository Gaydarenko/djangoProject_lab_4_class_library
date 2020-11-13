from django.urls import path
from .views import LibraryView, CreateView, AuthorsListView, CreateFormView, SearchView, BookFormView, BooksListView, BookView

urlpatterns = [
    path('', LibraryView.as_view()),
    path('create/', CreateView.as_view(), name='create'),
    path('authors/', AuthorsListView.as_view(), name='authors'),
    path('authors/<int:page>', AuthorsListView.as_view()),
    path('create-form/', CreateFormView.as_view(), name='create-form'),
    path('search/', SearchView.as_view(), name='search'),
    path('create_book/', BookFormView.as_view(), name='create-book'),
    path('books/', BooksListView.as_view(), name='books'),
    path('books/<int:page>', BooksListView.as_view()),
    path('book/', BookView.as_view(), name='book'),
    path('book/<int:id>', BookView.as_view()),
]
