import requests
from django.shortcuts import render
from django.http import JsonResponse
from .constants import BLOGS


def index(request):
    """
    Main page is just a template
    """
    return render(request, "index.html", {})


def news_collector_sync_view(request):
    """
    Synchronous HTTP fetcher
    """
    data = {}
    # Go through each blog and fetch it using requests
    for name, link in BLOGS.items():
        response = requests.get(link)
        if response.status_code != 200:
            data[name] = 'Download error'
        else:
            data[name] = response.content.decode("utf-8")
    return JsonResponse(data)
