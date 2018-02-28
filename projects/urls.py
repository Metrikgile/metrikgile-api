from django.urls import path

from projects.views import RegisterRepository

app_name = 'projects'

urlpatterns = [
    path('register/', RegisterRepository.as_view(),
         name="repo_registration"),
]
