from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import CreateCharacterForm, UpdateCharacterForm
from main.models import *


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'main/category.html'
    context_object_name = 'category'

    # для получения slug
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    # для получения данных о персонаже
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characters'] = Character.objects.filter(category_id=self.slug)
        return context


class CharacterDetailView(DetailView):
    model = Character
    template_name = 'main/character.html'
    context_object_name = 'character'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
<<<<<<< HEAD
        image = self.get_object().get_image
        context['images'] = self.get_object().exclude(id=image.id)
=======
>>>>>>> bd23f09a0a2e29b138762899145e1007b53eda4b
        return context


class GenreListView(ListView):
    model = Genre
    template_name = 'main/genre.html'
    context_object_name = 'genre'



class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_staff


<<<<<<< HEAD
class CharacterCreateView(CreateView):
=======
class CharacterCreateView(IsAdminMixin,CreateView):
>>>>>>> bd23f09a0a2e29b138762899145e1007b53eda4b
    model = Character
    template_name = 'main/create.html'
    form_class = CreateCharacterForm
    success_url = reverse_lazy('home')


<<<<<<< HEAD
class CharacterUpdateView(UpdateView):
    model = Character
=======
class CharacterUpdateView(IsAdminMixin,UpdateView):
    queryset = Character.objects.all()
>>>>>>> bd23f09a0a2e29b138762899145e1007b53eda4b
    form_class = UpdateCharacterForm
    template_name = 'main/update.html'
    context_object_name = 'character'


class CharacterDeleteView(IsAdminMixin,DeleteView):
    model = Character
    template_name = 'main/delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(request, messages.SUCCESS, 'Successfully deleted!')
        return HttpResponseRedirect(success_url)