import email
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import permissions, status
from user_account.serializers import LoginSerializer, ChangePasswordSerializer, OTPVerificationSerializer, EmailSerializer, UserDetailSerializer, UserRegistrationSerializer, UserLogoutSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User, Group
from .helpers.mail import signup_mail, send_otp_mail
from django.db import IntegrityError
from main.helpers.generators import generate_code
from django.utils import timezone
from .models import UserOtp
from django.shortcuts import get_object_or_404
from django.http import Http404


User = get_user_model()


class Welcome(APIView):
    def get(self, request):
        data = {
            "status": 200,
            "message": "Welcome to Nextpixie Backend"
        }
        return Response(data, status=200)
    

class UserRegisterView(APIView):
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        try:
            serializer.is_valid(raise_exception=True)
            account = serializer.save()
        except IntegrityError as e:
            data['response'] = 'error registering a new user.'
            data['error'] = str(e)
            return Response(data, status=400)
        data['response'] = 'successfully registered a new user.'
        data['id'] = account.id
        data['first_name'] = account.first_name
        data['last_name'] = account.last_name
        data['email'] = account.email

        return Response(data)


class AddUserGroups(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

        user = User.objects.get(email=request.user)
        group = Group.objects.get(id=1)
        user.groups.add(group)
        data = {
            "role": user.role,
            "message": f"user with email ({user.email}) as been verified and added to a user group"
        }

        return Response(data, 201)

class AllUsersView(ListAPIView):
    queryset = User.objects.filter(is_deleted=False)
    serializer_class = UserDetailSerializer


class ChangePasswordView(generics.GenericAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self):
            obj = self.request.user
            return obj

        def post(self, request):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                data = {
                    'status': 'success',
                    'message': 'Password updated successfully',
                }
                return Response(data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView):
    serializer_class = UserLogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"Status": "Successfully logged out!"}, status=status.HTTP_204_NO_CONTENT)



class UserLoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, email = serializer.validated_data['email'], password = serializer.validated_data['password'])
        if user and user.is_active:
            if user.status:
                try:
                    refresh = RefreshToken.for_user(user)
                    user_details = {}
                    user_details['id'] = user.id
                    user_details['email'] = user.email
                    user_details['role'] = user.role
                    user_details['access_token'] = str(refresh.access_token)
                    user_details['refresh_token'] = str(refresh)
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)

                    data = {
                        'message' : "User Login successful",
                        'data' : user_details,
                    }
                    return Response(data, status=status.HTTP_200_OK)
                
                except Exception as e:
                    raise e
        else:
            data = {
                'message'  : "failed",
                'errors': 'The account is not active'
                }
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class UserActions(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()




class RequestOtpMail(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        try:
            user = get_object_or_404(User, email=email)
        except Http404:
            return Response({"error": "user not found"}, status=404)
        
        otp = generate_code()
        expiry_date = timezone.now() + timezone.timedelta(minutes=5)

        UserOtp.objects.create(user=user, otp=otp, expiry_date=expiry_date)

        send_otp_mail(email=email, first_name=user.first_name, otp=otp)

        return Response({"message": "otp request successful", "otp": otp}, status=200)

class VerifyOtp(APIView):

    def post(self, request):

        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            otp = serializer.validated_data['otp']
            try:
                obj = UserOtp.objects.get(otp=otp)
            except UserOtp.DoesNotExist:
                return Response({"error": "Invalid Otp"}, status=400)
            if obj.is_valid():
                obj.delete()
                return Response({"message": "success"}, status=200)
            else:
                obj.delete()
                return Response({"error": "otp expired, request new otp"}, status=400)


class UserVerificationView(APIView):
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.user_verification_otp(request)
            return Response(data, status=200)
        
        else:
            return Response(serializer.errors, status=400)



class AllUsers(generics.ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.filter(is_deleted=False)


