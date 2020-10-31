from django.shortcuts import render
from django.views import View


# Create your views here.
class LibraryView(View):
    def get(self, request):
        return render(request, 'library/index.html')


class CreateView(View):
    def get(self, request):
        return render(request, 'library/create.html')

    def post(self, request):
        pass


class AuthorsView(View):
    def get(self, request):
        return render(request, 'library/authors.html')
