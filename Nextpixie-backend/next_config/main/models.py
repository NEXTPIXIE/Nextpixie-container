from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.

class UserAlbum(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    category = models.ForeignKey("main.UserCategories", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey("user_account.User", on_delete=models.CASCADE, null=True, related_name="users",blank=True)
    name = models.CharField(max_length=250, blank=False)
    caption = models.TextField(blank=False)
    album_tag = models.CharField(max_length=200)
    time_stamp = models.DateTimeField(auto_now_add=True)


class UserPhotos(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    album_id = models.ForeignKey("main.UserAlbum", on_delete=models.CASCADE, null=True, related_name="albums", blank=False)
    image = models.ImageField(blank=True, upload_to='images')
    time_stamp = models.DateTimeField(auto_now_add=True)


class UserCategories(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    owner = models.ForeignKey("user_account.User", on_delete=models.CASCADE, null=True, related_name="owners",blank=True)
    name = models.CharField(max_length=250, blank=True)
