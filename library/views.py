from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Author
from html import escape


# Create your views here.
class LibraryView(View):
    def get(self, request):
        return render(request, 'library/index.html')


class CreateView(View):
    def get(self, request):
        return render(request, 'library/create.html')

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
        return render(request, 'library/create_form.html')


