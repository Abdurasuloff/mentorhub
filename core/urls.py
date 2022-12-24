from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')), 
    path('article/', include('articles.urls')),
    path('course/', include('courses.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
