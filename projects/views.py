from django.http import HttpResponse, HttpResponseNotFound

import requests

from projects.serializers import RepositorySerializer

API_GITHUB_URL = 'https://api.github.com/repos/'


def get_repository(request, repo):
    repo_url = "{github}{repo}".format(github=API_GITHUB_URL, repo=repo)
    response = requests.get(repo_url)

    if response.status_code == 200:
        data = response.json()
        serializer = RepositorySerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return HttpResponse(status=200, content_type="application/json",
                                content=response.content)

    return HttpResponseNotFound()


