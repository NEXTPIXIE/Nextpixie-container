from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from djoser.signals import user_activated
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import UserOtp

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=100, default='basic user')
    client = serializers.CharField(max_length=100, default='user')
    password = serializers.CharField(style={"input_type": "password"}, write_only=True, required=True)

    class Meta():
        model = User
        fields = ['id', "first_name", "last_name", "business_name", 'role', "client", "email", "password"]

    def create(self, validate_data):

        return User.objects.create_user(**validate_data)


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class OTPVerificationSerializer(serializers.Serializer):
   
    otp = serializers.CharField(max_length=6)
    
    def user_verification_otp(self, request):
        otp = self.validated_data['otp']
        try:
            otp = get_object_or_404(UserOtp, otp=otp)
        except Http404:
            raise serializers.ValidationError(detail="OTP not found")
        if otp:
            if otp.is_valid():
                if otp.user.is_active == False:
                    otp.user.is_active=True
                    otp.user.is_verified=True
                    otp.user.save()

                    otp.delete()
                    user_activated.send(User, user=otp.user, request=request)
                    return {'message': 'Verification Complete'}
                else:
                    otp.delete()
                    raise serializers.ValidationError(detail='This user as been verified.')
            else:
                otp.delete()
                raise serializers.ValidationError(detail='OTP expired')
        else:
            raise serializers.ValidationError(detail="wahala wa oh!!!")
        


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=250)



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
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


