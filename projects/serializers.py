from rest_framework import serializers

from projects.models import Repository


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ('id', 'name', 'full_name', 'description',
                  'private', 'html_url')
