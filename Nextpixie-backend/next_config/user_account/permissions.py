from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed


from django.conf import settings
from rest_framework_simplejwt.settings import api_settings






class IsAdmin(permissions.BasePermission):
    """
    Allows access only to only admin users.
    """
    def has_permission(self, request, view):
        if request.user.is_admin:
            return  bool(request.user and request.user.is_authenticated)
        else:
            raise AuthenticationFailed(detail="Authentication credentials were not provided oh ")