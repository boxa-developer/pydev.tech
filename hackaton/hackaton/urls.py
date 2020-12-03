
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings


def index(request):
    return render(request, 'index.html')


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('cms/', include('cms.urls')),
                  path('', index)
              ] + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
