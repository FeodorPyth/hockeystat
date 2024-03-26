from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('admin', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
