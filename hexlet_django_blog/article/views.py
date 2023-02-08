from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    name = 'article'
    return render(
        request,
        'article/index.html',
        context={'app_name': name},
    )

