from django.http import HttpResponse
from django.conf import settings

def home(request):

    file_path = settings.BASE_DIR / 'bookapp' / 'static' / 'backcover.html'

    with open(file_path, 'r', encoding='utf-8') as file:
        return HttpResponse(file.read())