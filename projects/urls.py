from django.urls import path

from projects.views import get_repository

urlpatterns = [
    path('', get_repository, name="index"),
]
