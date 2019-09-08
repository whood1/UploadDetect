from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    # path('whats typed after url', view, name='name')
    path('upload_image', views.upload_image, name='upload_image'),
    path('index', views.index, name='index')
]