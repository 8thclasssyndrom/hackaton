from django.urls import path

from blog.views import *


urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('<slug:slug>/', blog_detail, name='blog-detail'),


]