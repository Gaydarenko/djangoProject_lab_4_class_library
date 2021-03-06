from html import escape

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage

from .models import Author, Book
from .forms import AuthorForm, BookForm, SearchForm


# Create your views here.
class LibraryView(View):
    def get(self, request):
        return render(request, 'library/index.html')


class CreateAuthorView(View):
    def get(self, request):
        return render(request, 'library/create_author.html')

    def post(self, request):
        data = request.POST
        try:
            author = Author(
                name=data['name'],
                surname=data['surname'],
                year=data['year']
            )
            author.save()
        except Exception:
            return HttpResponseBadRequest("Bad request")
        return HttpResponse(escape(author.name))    # escape для экранирования, если вдруг вместо имени кто-то будет
                                                    # передавать ссылку (чтобы ссылка не работала)


class AuthorsListView(View):
    def get(self, request, page=1):
        authors_on_list = 4
        authors = list(Author.objects.values())
        paginator = Paginator(authors, authors_on_list)

        try:
            authors = paginator.page(page)
            authors.pages = tuple(paginator.page_range)
        except EmptyPage:
            return redirect(reverse('authors'))

        return render(request, 'library/authors.html', context={'authors': authors})


class CreateAuthorFormView(View):
    def get(self, request):
        author_form = AuthorForm()
        return render(request, 'library/create_author_form.html', context={'author_form': author_form})

    def post(self, request):
        author_form = AuthorForm(request.POST)
        if not author_form.is_valid():
            return HttpResponseBadRequest("Bad request")

        data = author_form.cleaned_data     # cleaned_data - только валидные данные
        author = Author(**data)
        author.save()
        return HttpResponse(escape(author.name))


class AuthorView(View):
    def get(self, request, id=1):
        author = Author.objects.get(pk=id)
        return render(request, 'library/author.html', context={'author': author})


class SearchView(View):
    def get(self, request):
        search_form = SearchForm()
        return render(request, 'library/search.html', context={'search_form': search_form})

    def post(self, request):
        search_form = SearchForm(request.POST)
        query = Book.objects.values()
        if search_form.data['title']:
            query = query.filter(title=search_form.data['title'])
        if search_form.data['genre']:
            query = query.filter(genre=search_form.data['genre'])
        if search_form.data['year']:
            query = query.filter(year=search_form.data['year'])
        books_list = query.all()

        if isinstance(books_list, dict):
            books_list = [books_list, ]

        return render(request, 'library/books.html', context={'books_list': books_list})


class CreateBookFormView(View):
    def get(self, request):
        create_book_form = BookForm()
        return render(request, 'library/create_book.html', context={'create_book_form': create_book_form})

    def post(self, request):
        create_book_form = BookForm(request.POST)
        if not create_book_form.is_valid():
            return HttpResponseBadRequest("Некорректные данные")

        data = create_book_form.cleaned_data
        print(data)
        book = Book(**data)
        book.save()
        return HttpResponse(escape(book.title))


class BooksListView(View):
    def get(self, request, page=1):
        books_on_list = 4
        books_list = list(Book.objects.values())
        print(books_list)
        paginator = Paginator(books_list, books_on_list)

        try:
            books_list = paginator.page(page)
            books_list.count_pages = [i for i in range(1, paginator.num_pages + 1)]
        except EmptyPage:
            return redirect(reverse('books'))

        return render(request, 'library/books.html', context={'books_list': books_list})


class BookView(View):
    def get(self, request, id=1):
        book = Book.objects.get(pk=id)
        return render(request, 'library/book.html', context={'book': book})
