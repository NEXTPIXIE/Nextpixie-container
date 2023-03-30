from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import UserAlbum, UserPhotos, UserCategory
from .serializers import AlbumSerializer, ImageSerializer, CategorySerializer, CreateAlbumCategorySerializer
from .helpers.generators import generate_tag, encode_file
from django.shortcuts import get_object_or_404







class MainView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        if request.user.has_perm('user_account.can_create_album'):
            print(True)
        else:
            print(False)
        return Response({"wahala": "wahala"})


class UserAlbumView(APIView):
    queryset = UserAlbum.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if request.user.has_perm('user_account.can_create_album'):

            serializer = self.serializer_class(data=request.data)
            data = {}
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['album_tag'] = generate_tag()
            serializer.validated_data['user'] = request.user
            # serializer.validated_data['category'] = 
            serializer.save()
            data['response'] = 'successfully created an album.'
            return Response(data)
            


        
class GetAlbum(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.has_perm('user_account.can_view_album'):
            try:
                all_albums = UserAlbum.objects.filter(email=request.user)
            except UserAlbum.DoesNotExist:
                return Response({"error": "albums not available"}, status=404)
            
            serializer = AlbumSerializer(all_albums, many=True)
            data = {
                "albums": serializer.data
            }
            return Response(data)
        else:
            return Response({"message": "user is not permitted"}, status=401)
        

class UserImageView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ImageSerializer

    def post(self, request, id):
        if request.user.has_perm('user_account.can_create_album'):
            album = UserAlbum.objects.get(id=id)

            serializer = self.serializer_class(data=request.data)
            data = {}
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['album_id'] = album
            image = serializer.validated_data['image']
            print(image)
            serializer.save()
            data['response'] = 'successfully saved an image.'
            return Response(data)


class GetImages(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        if request.user.has_perm('user_account.can_view_album'):
            try:
                instance = UserPhotos.objects.filter(album_id=id)
                serializer = ImageSerializer(instance, many=True)
                return Response(serializer.data)
            except UserPhotos.DoesNotExist:
                return Response({"error": "album images not found"}, status=404)
        else:
            return Response({"message": "user not permitted"}, status=401)

class CategoryView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer
    
    def post(self, request):
        if request.user.has_perm('user_account.can_create_album'):

            serializer = self.serializer_class(data=request.data)
            data = {}
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['owner'] = request.user
            serializer.save()
            data['response'] = 'successfully created a category.'
            return Response(data)
        
    def get(self, request):
        if request.user.has_perm('user_account.can_view_album'):
            try:
                categories = UserCategory.objects.filter(email=request.user)
            except UserCategory.DoesNotExist:
                return Response({"error": "category not available"}, status=404)
            serializer = CategorySerializer(categories, many=True)
            data = {
                "categories": serializer.data
            }
            return Response(data)
        else:
            return Response({"message": "user is not permitted"}, status=401)

# class CategoryAlbumView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def post(self, request):
#         serializer = CreateAlbumCategorySerializer(data=request.data)

#         serializer.is_valid(raise_exception=True)
#         category = serializer.validated_data.pop('category')
#         album = serializer.validated_data.pop('album')
#         user_name = category['name']
#         user_category = get_object_or_404(UserCategory, name=user_name)
#         print(user_category)
#         if user_category:
#             user_album = UserAlbum.objects.create(category=user_category, user=request.user, album_tag=generate_tag(), **album)
#             data = {
#                 "message": "success",
#                 "album": AlbumSerializer(user_album).data
#             }

#             return Response(data, 200)
#         else:            
#             obj = UserCategory.objects.create(user=request.user, **category)
            
#             album_data = UserAlbum.objects.create(category=obj, user=request.user, album_tag=generate_tag(), **album)
            
#             data1 = {"message": "success", 
#                     "category": CategorySerializer(obj).data, 
#                     "album":AlbumSerializer(album_data).data
#                     }
            
#             return Response(data1, status=200)

from django.http import Http404

class CategoryAlbumView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = CreateAlbumCategorySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        category = serializer.validated_data.pop('category')
        album = serializer.validated_data.pop('album')
        user_name = category['name']
        
        try:
            user_category = get_object_or_404(UserCategory, name=user_name)
        except Http404:
            obj = UserCategory.objects.create(user=request.user, **category)
            
            album_data = UserAlbum.objects.create(category=obj, user=request.user, album_tag=generate_tag(), **album)
            
            data1 = {"message": "success", 
                    "category": CategorySerializer(obj).data, 
                    "album":AlbumSerializer(album_data).data
                    }
            
            return Response(data1, status=200)
        
        user_album = UserAlbum.objects.create(category=user_category, user=request.user, album_tag=generate_tag(), **album)
        data = {
            "message": "success",
            "album": AlbumSerializer(user_album).data
        }

        return Response(data, 200)
