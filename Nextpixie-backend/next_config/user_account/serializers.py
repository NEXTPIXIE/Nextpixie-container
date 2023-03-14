from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.response import Response
from rest_framework import status
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=100, default='staff')
    password = serializers.CharField(style={"input_type": "password"}, write_only=True, required=False)

    class Meta():
        model = User
        fields = ['id', "name", "email", 'role', "password"]

    def create(self, validate_data):

        return User.objects.create_user(**validate_data)

class AdminRegistrationSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=100, default='admin')
    password = serializers.CharField(style={"input_type": "password"}, write_only=True, required=False)


    class Meta:
        model = User
        fields = ["id", "name", "email", "role", "password"]

    def create(self, validated_data):
        return User.objects.create_admin(**validated_data)

        


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=700)
    password = serializers.CharField(max_length=700)




class UserLogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:

        	return Response({"message": "failed", "error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordSerializer(serializers.Serializer):
    # email = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


