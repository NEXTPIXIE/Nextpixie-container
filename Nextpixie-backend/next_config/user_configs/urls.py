from django.urls import path

from . import views


urlpatterns = [
    path('user/profile', views.ProfileView.as_view()),
    path('security/alert', views.AddSecurityAlert.as_view())
    


]