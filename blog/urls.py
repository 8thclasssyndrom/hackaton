from django.urls import path

from blog.views import post_list, post_detail


urlpatterns = [
    path('', post_list, name='post-list'),
    path('<str:slug>/', post_detail, name='post-detail'),


]