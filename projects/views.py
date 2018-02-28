import requests
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from projects.serializers import RepositorySerializer

API_GITHUB_URL = 'https://api.github.com/repos/'


class RegisterRepository(generics.CreateAPIView):
    """ Register a new repository """

    serializer_class = RepositorySerializer

    def get_post_data(self, request):
        repo_name = ''

        try:
            repo_name = request.POST['repository_name']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return repo_name

    def get_github_repository(self, repository_name):
        repo_url = "{github}{repo}".format(github=API_GITHUB_URL,
                                           repo=repository_name)
        response = requests.get(repo_url)
        data = {}

        if response.status_code == 200:
            data = response.json()

        return data

    def create(self, request):
        repo_name = self.get_post_data(request)
        data = self.get_github_repository(repo_name)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
