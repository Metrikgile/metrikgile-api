from django.http import HttpResponse, HttpResponseNotFound
import requests


def get_repository(request):
    url = 'https://api.github.com/repos/Metrikgile/metrikgile-api'
    response = requests.get(url)
    if response.status_code == 200:
        return HttpResponse(status=200)

    return HttpResponseNotFound()


