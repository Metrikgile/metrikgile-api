from django.urls import reverse
import pytest

from projects.models import Repository

pytestmark = pytest.mark.django_db


@pytest.fixture
def register_project_url():
    url = reverse('projects:repo_registration')

    return url


def test_post_repository_registration_return_400(client, register_project_url):
    """ Test whether the application returns 400 for a post
    on repository registration url with invalid data """

    data = {}
    response = client.post(register_project_url, data=data)

    assert response.status_code == 400


def test_get_project_return_200(client, register_project_url):
    """ Test whether a get on projects url return 200"""

    data = {'repository_name': 'Metrikgile/metrikgile-api'}
    response = client.post(register_project_url, data=data)

    assert response.status_code == 201


def test_get_project_return_not_null_content(client, register_project_url):
    """ Test non empty content for a get in project url"""

    response = client.get(register_project_url)

    assert response.json()


def test_get_repository_on_response(client, register_project_url):
    """ Test repository information returned in the content """

    response = client.get(register_project_url)

    assert response.json()['name'] == 'metrikgile-api'


def test_new_repository_registration(client, register_project_url):
    """ Test whether the method register a new repository on db """

    response = client.get(register_project_url)

    assert Repository.objects.count() == 1
    assert Repository.objects.first().name == 'metrikgile-api'

