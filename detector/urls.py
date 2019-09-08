from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('index', views.index, name='index'),
    path('detect', views.detect, name='detect')
]