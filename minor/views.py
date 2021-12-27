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

    # def get_template_names(self):
    #     template_name = super(MainPageView, self).get_template_names()
    #     search = self.request.GET.get('search')
    #     if search:
    #         template_name = 'search.html'
    #     return template_name
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     search = self.request.GET.get('search')
    #     if search:
    #         context['categories'] = Category.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
    #
    #     else:
    #         context['categories'] = Category.objects.all()
    #     return context
    #


def contacts(request):
        return render(request, 'minor/contacts.html')


# тоже типо-мини-блог
# можно добавить пару смешных статей про аниме
def blog(request):
    return render(request, 'minor/blog.html')

