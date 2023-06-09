from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User, Permission
from .models import UserProfile
from django.http import Http404
import json
from .serializers import ProfileSerializer
from main.helpers.generators import generate_tag
from django.contrib.auth import get_user_model
User = get_user_model()
import requests

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
        
    def get(self, request):
        if request.user.has_perm('user_account.can_create_album'):
            try:
                profile = UserProfile.objects.get(user=request.user.id)
                serializer = ProfileSerializer(profile)
                return Response({"profile": serializer.data})
            except UserProfile.DoesNotExist:
                return Response({"error": "profile not found"}, status=404)
        else:
            return Response({"erorr": "user is not permitted"}, 404)

    def put(self, request):
        if request.user.has_perm('user_account.can_create_album'):
            profile = UserProfile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile, partial=True)
            data = {
                "message": "edited user profile",
                "data": serializer.data
            }
            return Response(data, status=200)


class AddSecurityAlert(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user = User.objects.get(email=request.user)
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

class AccessNotification(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='album_notification')
            user.user_permissions.add(permission)
            data = {
                "message": f"notification alert as been added to user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
        
    def delete(self, request):
        try:
            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='album_notification')
            user.user_permissions.remove(permission)
            data = {
                "message": f"notification alert as been removed from user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)



class DownloadNotification(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='download_notification')
            user.user_permissions.add(permission)
            data = {
                "message": f"download alert as been added to user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
        
    def delete(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='download_notification')
            user.user_permissions.remove(permission)
            data = {
                "message": f"download alert as been removed from user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)


class FavoritesNotification(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='favorites_notification')
            user.user_permissions.add(permission)
            data = {
                "message": f"favorites notification alert as been added to user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
        
    def delete(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='favorites_notification')
            user.user_permissions.remove(permission)
            data = {
                "message": f"favorites notification alert as been removed from user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)


class CommentNotification(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='comment_notification')
            user.user_permissions.add(permission)
            data = {
                "message": f"comment alert as been added to user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
        
    def delete(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='comment_notification')
            user.user_permissions.remove(permission)
            data = {
                "message": f"comment alert as been removed from user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)



class AllowUsersViewProfile(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='users_can_view_profile')
            user.user_permissions.add(permission)
            data = {
                "message": f"profile permission as been added to user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
        
    def delete(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='users_can_view_profile')
            user.user_permissions.remove(permission)
            data = {
                "message": f"profile permission as been removed from user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
        

class UsersCanDownload(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='users_can_download')
            user.user_permissions.add(permission)
            data = {
                "message": f"User download permission as been added to user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
        
    def delete(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='users_can_download')
            user.user_permissions.remove(permission)
            data = {
                "message": f"user download permission as been removed from user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)


class UsersFavorite(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='users_can_favorite')
            user.user_permissions.add(permission)
            data = {
                "message": f"user favorite permission as been added to user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
        
    def delete(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='users_can_favorite')
            user.user_permissions.remove(permission)
            data = {
                "message": f"user favorite permission as been removed from user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)


class UsersComment(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='users_can_comment')
            user.user_permissions.add(permission)
            data = {
                "message": f"comment permission as been added to user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
        
    def delete(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='users_can_comment')
            user.user_permissions.remove(permission)
            data = {
                "message": f"comment permission as been removed from user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)



class UsersSharing(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='users_can_share')
            user.user_permissions.add(permission)
            data = {
                "message": f"users sharing permission as been added to user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)
        
    def delete(self, request):
        try:

            user = User.objects.get(email=request.user)
            permission = Permission.objects.get(codename='users_can_share')
            user.user_permissions.remove(permission)
            data = {
                "message": f"users sharing permission as been removed from user {user.email}"
            }
            return Response(data, 200)
        except:
            return Response({"error": "user not found"}, 404)


class GetUserLocation(APIView):
    def get(self, request):
        try:
            url = "http://ip-api.com/json/"

            response = requests.get(url=url)
            valid = json.loads(response.text)
            data = {
                "location": valid
            }
            return Response(data, status=200)
        except requests.exceptions.HTTPError:
            return Response({"error": "location undefined"}, status=400)
