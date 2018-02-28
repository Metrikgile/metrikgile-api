from django.urls import path

from projects.views import RegisterRepository
from projects.views import RepositoryDetail

app_name = 'projects'

urlpatterns = [
    path('register/', RegisterRepository.as_view(),
         name="repo_registration"),

    path('<int:pk>', RepositoryDetail.as_view(), name="repo_detail")
]
