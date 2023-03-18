from django.contrib.auth import authenticate, get_user_model
import os
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def split_name(name):
    first_name, last_name = name.split(" ")
    return first_name.title(), last_name.title()


def register_social_user(provider, user_id,email, name):
    filtered_user_by_email = User.objects.filter(email=email, is_deleted=False)

    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].client_provider:

            registered_user = authenticate(
                email=email, password=os.getenv('SOCIAL_SECRET'))
            
            refresh = RefreshToken.for_user(registered_user)
            return {
                'id':registered_user.id,
                'first_name': registered_user.first_name,
                'last_name':registered_user.last_name,
                'email': registered_user.email,
                'role':registered_user.role,
                "phone":registered_user.phone,
                'is_admin':registered_user.is_admin,
                'refresh': str(refresh),
                'access' : str(refresh.access_token)
            }


        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].client_provider)

    else:
        first_name, last_name = split_name(name)
        user = {
            'first_name': first_name, 
            'last_name' :last_name,
            'email': email,
            'phone':None,
            'role': 'user',
            'password': os.getenv('SOCIAL_SECRET')}
        
        user = User.objects.create_user(**user)
        user.is_active = True
        user.client_provider = provider
        user.save()
        
        print(user.id)

        new_user = authenticate(
            email=user.email, password=os.getenv('SOCIAL_SECRET'), is_deleted=False)
        
        print(new_user)
        
        refresh = RefreshToken.for_user(new_user)
        return {
                'id':user.id,
                'first_name': user.first_name,
                'last_name':user.last_name,
                'email': user.email,
                'role':user.role,
                "phone" : user.phone,
                'is_admin':user.is_admin,
                'refresh': str(refresh),
                'access' : str(refresh.access_token)
            }
