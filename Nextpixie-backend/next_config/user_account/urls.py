from django.urls import path, include
from .views import UserRegisterView, AllUsersView, UserLoginView, LogoutView, ChangePasswordView
from rest_framework_simplejwt.views import TokenRefreshView   
from rest_framework_simplejwt.views import TokenVerifyView




urlpatterns = [
    path('register/user', UserRegisterView.as_view()),
    path('all_users', AllUsersView.as_view()),
    path('user/login', UserLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('password', ChangePasswordView.as_view()),
    path('refresh', TokenRefreshView().as_view(), name="refresh_token"),
    path('auth/', include('djoser.urls')),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify')

]
