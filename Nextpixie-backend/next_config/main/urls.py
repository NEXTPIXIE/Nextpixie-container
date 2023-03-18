from django.urls import path

from .views import MainView
from . import views


urlpatterns = [
    path('test', MainView.as_view()),
    path('album/create', views.UserAlbumView.as_view()),
    path('album/all', views.GetAlbum.as_view())


]