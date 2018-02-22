import pytest

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
