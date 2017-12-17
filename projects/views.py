from django.shortcuts import render
import requests

class GetIssues():
    url = 'https://api.github.com/repos/Metrikgile/metrikgile-api/issues'
    response = requests.get(url)


