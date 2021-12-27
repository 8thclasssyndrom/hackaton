from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.views import *
from minor.views import *

urlpatterns = [
    path('', MainPageView.as_view(), name="home"),
    path('contacts/', contacts, name='contacts'),
    path('blog/', blog, name='blog'),
    path('genre/', GenreListView.as_view(), name="genre"),
]
