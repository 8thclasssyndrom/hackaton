from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.db.models import Q

from main.models import Category


# используем здесь листвью, чтобы увидеть наши категории
class MainPageView(ListView):
    model = Category
    template_name = 'minor/index.html'
    context_object_name = 'categories'
    paginate_by = 3


def contacts(request):
        return render(request, 'minor/contacts.html')


# тоже типо-мини-блог
# можно добавить пару смешных статей про аниме

class SearchResultsView(View):
    def get(self, request):
        queryset = None
        search_param = request.GET.get('search')
        if search_param is not None:
            queryset = Category.objects.filter(Q(name__icontains=search_param)|Q(description__icontains=search_param))
        return render(request, 'minor/index.html', {'categories': queryset})
