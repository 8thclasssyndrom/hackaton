from django.shortcuts import render
from django.views.generic import ListView

from main.models import Category


# используем здесь листвью, чтобы увидеть наши категории
class MainPageView(ListView):
    model = Category
    template_name = 'minor/index.html'
    context_object_name = 'categories'


# это для, того чтобы дописать наши контакты и почты
# надеюсь сможешь добавить инфу в темплейтку
def contacts(request):
    return render(request, 'minor/contacts.html')


# тоже типо-мини-блог
# можно добавить пару смешных статей про аниме
def blog(request):
    return render(request, 'minor/blog.html')

