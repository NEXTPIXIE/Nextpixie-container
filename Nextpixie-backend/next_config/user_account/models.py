from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from django.utils import timezone

import uuid


class User(AbstractBaseUser, PermissionsMixin):
    
    
    id            = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    first_name    = models.CharField(_('first name'),max_length = 250)
    last_name     = models.CharField(_('last name'),max_length = 250)
    business_name = models.CharField(_('business_name'),max_length=250)
    role          = models.CharField(_('role'), max_length = 250)
    client        = models.CharField(_('client'),max_length=250)
    email         = models.EmailField(_('email'), unique=True)
    status        = models.BooleanField(_('status'), default=False)
    password      = models.CharField(_('password'), max_length=300)
    is_staff      = models.BooleanField(_('staff'), default=False)
    is_admin      = models.BooleanField(_('admin'), default= False)
    is_active     = models.BooleanField(_('active'), default=True)
    is_deleted    = models.BooleanField(_('deleted'), default=False) 
    date_joined   = models.DateTimeField(_('date joined'), auto_now_add=True)
    client_provider = models.CharField(_('client_provider'), max_length=200, default='self_auth', null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role', 'client', 'password']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
    





    class Meta:
        permissions = [
            ("users_can_view_profile", "Users Can View Profile"),
            ("users_can_download", "Users Can Download"),
            ("users_can_favorite", "Users Can Favorite"),
            ("users_can_comment", "Users Can Comment"),
            ("users_can_share", "Users Can Share"),
            ("can_create_album", "Can Create Album"),
            ("can_view_album", "Can View Album"),
            ("can_publish_album", "Can Publish Album"),
            ("security_alert", "Security Alert"),
            ("album_notification", "Album Notification"),
            ("download_notification", "Download Notification"),
            ("favorites_notification", "Favorites Notification"),
            ("comment_notification", "Comment Notification")
            
        ]

class UserOTP(models.Model):
    otp = models.IntegerField(null=True, blank=False)
    timestamp = models.DateTimeField(default=timezone.now)



