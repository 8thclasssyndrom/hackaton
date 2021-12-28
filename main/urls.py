from django.urls import path

from main.views import *

urlpatterns = [
    path('<str:slug>/', CategoryDetailView.as_view(), name="category"),
    path('', CategoryListView.as_view(), name='category-list'),
    path('character/<int:pk>/', CharacterDetailView.as_view(), name="character"),
    path('character/<int:pk>/update', CharacterUpdateView.as_view(), name='update'),
    path('character/<int:pk>/delete', CharacterDeleteView.as_view(), name='delete'),

]