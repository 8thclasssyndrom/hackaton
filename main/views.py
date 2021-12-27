from django.shortcuts import redirect
from django.urls import reverse_lazy
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
        image = self.get_object().get_image
        context['images'] = self.get_object().images.exclude(id=image.id)
        return context


class GenreListView(ListView):
    model = Genre
    template_name = 'main/genre.html'
    context_object_name = 'genre'


class CharacterCreateView(CreateView):
    model = Character
    template_name = 'main/create.html'
    form_class = CreateCharacterForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['character_form'] = self.get_form(self.get_form_class())
        return context


class CharacterUpdateView(UpdateView):
    model = Character
    form_class = UpdateCharacterForm
    template_name = 'main/update.html'
    pk_url_kwarg = 'character_id'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['character_form'] = self.get_form(self.get_form_class())
        return context


class CharacterDeleteView(DeleteView):
    model = Character
    template_name = 'main/delete.html'
    pk_url_kwarg = 'character_id'
    success_url = 'home'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('home')
