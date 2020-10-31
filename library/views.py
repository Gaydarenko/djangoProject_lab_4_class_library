from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.
class LibraryView(View):
    def get(self, request):
        return render(request, 'library/index.html')


class CreateView(View):
    def get(self, request):
        return render(request, 'library/create.html')

    def post(self, request):
        data = request.POST
        print(data)
        print(data['name'])
        return HttpResponse()



class AuthorsView(View):
    def get(self, request):
        return render(request, 'library/authors.html')
