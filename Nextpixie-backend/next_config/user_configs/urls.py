from django.urls import path

from . import views


urlpatterns = [
    path('user/profile', views.ProfileView.as_view()),
    path('security/alert', views.AddSecurityAlert.as_view()),
    path('access/notification', views.AccessNotification.as_view()),
    path('favorites/notification', views.FavoritesNotification.as_view()),
    path('allow/users/view', views.AllowUsersViewProfile.as_view()),
    path('allow/users/download', views.UsersCanDownload.as_view()),
    path('allow/users/favorite', views.UsersFavorite.as_view()),
    path('allow/users/comment', views.UsersComment.as_view()),
    path('allow/users/share', views.UsersSharing.as_view()),
    path('user/location', views.GetUserLocation.as_view())



] 
