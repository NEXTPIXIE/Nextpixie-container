from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView   
from rest_framework_simplejwt.views import TokenVerifyView




urlpatterns = [
    path('register/user', views.UserRegisterView.as_view()),
    path('all_users', views.AllUsersView.as_view()),
    path('user/login', views.UserLoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('password', views.ChangePasswordView.as_view()),
    path('refresh', TokenRefreshView().as_view(), name="refresh_token"),
    path('auth/', include('djoser.urls')),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('djoser/', include('djoser.urls')),
    path('user/groups', views.AddUserGroups.as_view()),
    path('verify/otp', views.OTPVerificationView.as_view()),
    path('request/otp', views.RequestOTP.as_view()),
    path('reset/password', views.ResetPassword.as_view()),
    path('user/actions/<str:pk>', views.UserActions.as_view())

]
