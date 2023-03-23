from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
User = get_user_model()



class ProfileSerializer(serializers.ModelSerializer):
    profile_tag = serializers.CharField(max_length=200, required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = models.UserProfile
        fields = [
            'id',
            'user',
            'profile_tag',
            'profile_picture',
            'user_category',
            'user_url',
            'user_bio'


        ]