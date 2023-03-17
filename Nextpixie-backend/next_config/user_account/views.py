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
from user_account.serializers import LoginSerializer, ChangePasswordSerializer, UserDetailSerializer, UserRegistrationSerializer, UserLogoutSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User, Group
User = get_user_model()






class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        data['response'] = 'successfully registered a new user.'
        data['email'] = account.email
        data['first_name'] = account.first_name
        data['last_name'] = account.last_name

        return Response(data)
    
class AddUserGroups(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        user = User.objects.get(email=request.user)
        group = Group.objects.get(name='user')
        user.groups.add(group)

        return Response({"message": "verified user group"}, 201)


"""
Adding users to groups once the account is been created
How tf do i create groups and add permissions seperately 

"""
class AllUsersView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    




class UserLoginView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, email = serializer.validated_data['email'], password = serializer.validated_data['password'])
        if user and user.is_active:
            if user.is_staff:
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