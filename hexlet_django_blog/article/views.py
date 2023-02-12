from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
class IndexView(View):

    def get(self, request, tags, article_id):
        return HttpResponse(f'Статья номер {article_id}. Тег {tags}')

