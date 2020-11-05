from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Author
from html import escape
from .forms import AuthorForm, BookForm


# Create your views here.
class LibraryView(View):
    def get(self, request):
        return render(request, 'library/index.html')


class CreateView(View):
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


class AuthorsView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'library/authors.html', context={'authors': authors})


class CreateFormView(View):
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


class SearchView(View):
    def get(self, request):
        return HttpResponse('1')


class BookView(View):
    def get(self, request):
        create_book_form = BookForm()
        return render(request, 'library/create_book.html', context={'create_book_form': create_book_form})
