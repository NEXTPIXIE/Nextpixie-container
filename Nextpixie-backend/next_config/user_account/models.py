
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone
from .managers import UserManager
import uuid


class User(AbstractBaseUser, PermissionsMixin):
    
    
    id            = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    first_name    = models.CharField(_('first name'),max_length = 250)
    last_name     = models.CharField(_('last name'),max_length = 250)
    business_name = models.CharField(_('business_name'),max_length=250)
    role          = models.CharField(_('role'), max_length = 250)
    client        = models.CharField(_('client'),max_length=250)
    email         = models.EmailField(_('email'), unique=True)
    password      = models.CharField(_('password'), max_length=300)
    is_staff      = models.BooleanField(_('staff'), default=False)
    is_admin      = models.BooleanField(_('admin'), default= False)
    is_active     = models.BooleanField(_('active'), default=True)
    date_joined   = models.DateTimeField(_('date joined'), auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id', 'first_name', 'last_name', 'role', 'phone', ]
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email