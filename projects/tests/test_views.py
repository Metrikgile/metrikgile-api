import pytest

from projects.models import Repository

pytestmark = pytest.mark.django_db


@pytest.fixture
def project_url():
    project = 'Metrikgile/metrikgile-api'
    url = '/projects/{}'.format(project)

    return url


def test_get_project_return_200(client, project_url):
    """ Test whether a get on projects url return 200"""

    response = client.get(project_url)

    assert response.status_code == 200


def test_get_project_return_not_null_content(client, project_url):
    """ Test non empty content for a get in project url"""

    response = client.get(project_url)

    assert response.json()


def test_get_repository_on_response(client, project_url):
    """ Test repository information returned in the content """

    response = client.get(project_url)

    assert response.json()['name'] == 'metrikgile-api'


def test_new_repository_registration(client, project_url):
    """ Test whether the method register a new repository on db """

    response = client.get(project_url)

    assert Repository.objects.count() == 1
    assert Repository.objects.first().name == 'metrikgile-api'

