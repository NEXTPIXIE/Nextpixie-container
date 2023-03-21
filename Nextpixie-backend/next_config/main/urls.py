from django.urls import path

from .views import MainView
from . import views


urlpatterns = [
    path('test', MainView.as_view()),
    path('album/create', views.UserAlbumView.as_view()),
    path('album/all', views.GetAlbum.as_view()),
    path('upload/image/<str:id>', views.UserImageView.as_view()),
    path('album/images/<str:id>', views.GetImages.as_view()),
    path('category', views.CategoryView.as_view()),
    


]