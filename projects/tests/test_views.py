import pytest

pytestmark = pytest.mark.django_db


def test_get_issues_from_github(client):
    response = client.get('/projects/')

    assert response.status_code == 200

