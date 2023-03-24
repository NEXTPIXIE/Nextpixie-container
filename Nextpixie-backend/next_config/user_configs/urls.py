from django.urls import path

from . import views


urlpatterns = [
    path('user/profile', views.ProfileView.as_view()),
    path('security/alert', views.AddSecurityAlert.as_view()),
    path('access/notification', views.AccessNotification.as_view()),
    path('favorites/notification', views.FavoritesNotification.as_view()),
    path('comment/notification', views.CommentNotification.as_view())
    
    


]