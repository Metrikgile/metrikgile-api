from django.db import models


class Repository(models.Model):
    name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    private = models.BooleanField()
    html_url = models.URLField()

    def __str__(self):
        return self.name
