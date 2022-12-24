from django.urls import path
from .views import index
from django.conf.urls import handler404

app_name='main'
urlpatterns = [
    path('', index, name='index')
]

handler404 = 'main.views.error_404'