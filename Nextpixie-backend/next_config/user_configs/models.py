from django.db import models
import uuid

# Create your models here.


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField("user_account.User", on_delete=models.CASCADE, null=True, related_name="userprofile",blank=True)
    profile_tag = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='images')
    user_category = models.CharField(max_length=200, blank=True, null=True)
    user_url = models.URLField(max_length=200, blank=True, null=True)
    user_bio = models.CharField(max_length=800, blank=True, null=True)

