from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main/main.html'


class SearchView(TemplateView):
    template_name = 'main/search.html'
