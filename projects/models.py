from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    private = models.BooleanField()
    html_url = models.URLField()
    contributors = models.ManyToManyField('Contributor',
                                          through='Contribution',
                                          related_name="repositories")

    def contributor_add(self, pk, num_contributions=0):
        contributor = Contributor.objects.get(pk=pk)
        self.contributions.create(repository=self, contributor=contributor,
                                  num_contributions=num_contributions)

        return self

    def __str__(self):
        return self.name


class Contributor(models.Model):
    login = models.CharField(max_length=20)

    def repository_add(self, pk, num_contributions=0):
        repository = Repository.objects.get(pk=pk)
        self.contributions.create(repository=repository, contributor=self,
                                  num_contributions=num_contributions)

        return self


class Contribution(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE,
                                   related_name="contributions")
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE,
                                    related_name="contributions")
    num_contributions = models.IntegerField(default=0)


