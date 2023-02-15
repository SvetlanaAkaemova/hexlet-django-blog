from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse


class HomePageView(TemplateView):

    template_name = 'base.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


def about(request):
    return render(request, 'about.html')


def index(request):
    return redirect(
        reverse('article', kwargs={'tags': 'python', 'article_id': 42})
    )
