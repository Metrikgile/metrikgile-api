import pytest

from projects.views import *

pytestmark = pytest.mark.django_db

def test_get_issues_from_github(client): 
    response = GetIssues.response
    data = response.json()
    assert response.status_code == 200
    assert data[0]['repository_url'] == 'https://api.github.com/repos/Metrikgile/metrikgile-api'

