from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, ObjectDoesNotExist):
            return HttpResponse(f'not found', status=404)