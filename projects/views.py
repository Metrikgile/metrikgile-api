from django.http import HttpResponse, HttpResponseNotFound
import requests

API_GITHUB_URL = 'https://api.github.com/repos/'


def get_repository(request, repo):
    repo_url = "{github}{repo}".format(github=API_GITHUB_URL, repo=repo)
    response = requests.get(repo_url)

    if response.status_code == 200:
        return HttpResponse(status=200, content_type="application/json",
                            content=response.content)

    return HttpResponseNotFound()


