from django.urls import path

from projects.views import get_repository

urlpatterns = [
    path('<path:repo>', get_repository, name="index"),
]
