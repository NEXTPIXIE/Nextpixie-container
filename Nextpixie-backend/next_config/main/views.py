from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import UserAlbum, UserPhotos
from .serializers import AlbumSerializer
from .helpers.generators import generate_album_tag
# Create your views here.





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

            # try:

            serializer = self.serializer_class(data=request.data)
            data = {}
            serializer.is_valid(raise_exception=True)
            serializer.validated_data['album_tag'] = generate_album_tag()
            serializer.validated_data['user'] = request.user
            serializer.save()
            data['response'] = 'successfully created an album.'
            return Response(data)
            


        
class GetAlbum(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.has_perm('user_account.can_create_album'):
            try:
                all_albums = UserAlbum.objects.all()
            except UserAlbum.DoesNotExist:
                return Response({"error": "albums not available"}, 404)
            serializer = AlbumSerializer(all_albums, many=True)
            data = {
                "all album": serializer.data
            }
            return Response(data)
        

        