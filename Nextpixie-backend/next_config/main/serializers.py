from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
User = get_user_model()



class AlbumSerializer(serializers.ModelSerializer):
    album_tag = serializers.CharField(max_length=200, required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=models.UserCategory.objects.all(), required=False)
    class Meta:
        model = models.UserAlbum
        fields = [
            'id',
            'category',
            'user',
            'name',
            'caption',
            'album_tag',
            'time_stamp'
        ]


class ImageSerializer(serializers.ModelSerializer):
    album_id = serializers.PrimaryKeyRelatedField(queryset=models.UserAlbum.objects.all(), required=False)
    class Meta:
        model = models.UserPhotos
        fields = [
            'id',
            'album_id',
            'image',
            'time_stamp'

        ]

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = models.UserCategory
        fields = [
            'id',
            'user',
            'name'
        ]

class CreateAlbumCategorySerializer(serializers.Serializer):
    category = CategorySerializer()
    album = AlbumSerializer()