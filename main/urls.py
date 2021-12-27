from django.urls import path

from main.views import *

urlpatterns = [
    path('<str:slug>/', CategoryDetailView.as_view(), name="category"),
    path('character/<int:pk>/', CharacterDetailView.as_view(), name="character"),
    path('character/<int:pk>/update', CharacterUpdateView.as_view(), name='update'),
    path('character/<int:pk>/delete', CharacterDetailView.as_view(), name='delete'),
    path('create/', CharacterCreateView.as_view(), name='create'),

]