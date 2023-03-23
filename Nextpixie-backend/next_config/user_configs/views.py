from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User, Permission
from .models import UserProfile
from .serializers import ProfileSerializer
from main.helpers.generators import generate_tag
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.



class ProfileView(APIView):
    
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if request.user.has_perm('user_account.can_create_album'):

            serializer = self.serializer_class(data=request.data)
            data = {}
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['profile_tag'] = generate_tag()
            serializer.validated_data['user'] = request.user
            serializer.save()
            data['response'] = 'successfully created profile.'
            return Response(data)
            

class AddSecurityAlert(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:

            user = User.objects.get(email=request.user)
            print(user)
            permission = Permission.objects.get(codename='security_alert')
            user.user_permissions.add(permission)
            data = {
                "message": f"security alert as been added to user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
    def delete(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='security_alert')
            user.user_permissions.remove(permission)
            data = {
                "message": f"security alert as been removed from user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)

