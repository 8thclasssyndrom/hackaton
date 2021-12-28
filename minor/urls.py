from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from minor.views import *

urlpatterns = [
    path('', MainPageView.as_view(), name="home"),
    path('contacts/', contacts, name='contacts'),
    path('blog/', blog, name='blog'),
    path('search', SearchResultsView.as_view(), name='search'),
]
