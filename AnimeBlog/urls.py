from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from main.views import CharacterCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('minor.urls')),
    path('category/', include('main.urls')),
    path('create/', CharacterCreateView.as_view(), name='create'),
    path('account/', include('account.urls')),
    path('post/', include('blog.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
