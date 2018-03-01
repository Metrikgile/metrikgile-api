import pytest
from model_mommy import mommy

pytestmark = pytest.mark.django_db


def test_add_contributor_on_repository():
    """ Test add_contributor method on Repository model """
    contributor = mommy.make('Contributor')
    repository = mommy.make('Repository')

    repository.contributor_add(contributor.id)

    assert repository.contributions.first().contributor == contributor


def test_add_repository_on_contributor():
    """ Test add_repository method on Contributor model """
    repository = mommy.make('Repository')
    contributor = mommy.make('Contributor')

    contributor.repository_add(repository.id)

    assert contributor.contributions.first().repository == repository
