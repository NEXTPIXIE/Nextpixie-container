"""
Django settings for next_config project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, seee
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""


from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from django.utils.timezone import timedelta
import os

load_dotenv(find_dotenv())


ENVIRONMENT=os.getenv("ENVIRONMENT")
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")

if ENVIRONMENT.title() == "Development":
    
    ALLOWED_HOSTS = []

    DEBUG = True

    DATABASES = {
        'default' : {
            'ENGINE' : 'django.db.backends.sqlite3',
            'NAME' : BASE_DIR/ 'db.sqlite3'
        }
    }
    

else:
    
    ALLOWED_HOSTS = ['nextpixie-container-production.up.railway.app']
    DEBUG = True
    
    CORS_ALLOW_ALL_ORIGIN = True
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOW_CREDENTIALS = True
    
        
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("db_name"),
            'HOST': os.getenv("db_host"),
            'USER': os.getenv("db_user"),
            'PASSWORD': os.getenv("db_password"),
            'PORT': os.getenv("db_port")

        }
    }
    
    
    # LOGGING = {
    #     'version': 1,
    #     'disable_existing_loggers': False,
    #     'handlers': {
    #         'file': {
    #             'level': 'DEBUG',
    #             'class': 'logging.FileHandler',
    #             'filename': os.path.join(BASE_DIR, 'resolute.log'),
    #         },
    #     },
    #     'loggers': {
    #         'django': {
    #             'handlers': ['file'],
    #             'level': 'DEBUG',
    #             'propagate': True,
    #         },
    #     },
    # }
    
    SESSION_COOKIE_SECURE = False
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_HOST = None
    SECURE_SSL_REDIRECT = False
    SECURE_PROXY_SSL_HEADER =(
        ('HTTP_X_FORWARDED_PROTO', 'https')
    )
    CSRF_COOKIE_SECURE=False
    
    

CORS_ALLOW_ALL_ORIGIN = True
CORS_ALLOW_HEADERS = [
    'baggage',
    'content-type',
    'authorization',
    'sentry-trace'
    ]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',



    #third_party apps
    'django_user_agents',
    'cloudinary_storage',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',


    #local apps
    'user_account',
    'main',
    'socialauth',
    'user_configs'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'next_config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'next_config.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'user_account.User'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'UPDATE_LAST_LOGIN': True,
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'BLACKLIST_AFTER_ROTATION': True,
}




REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework_simplejwt.authentication.JWTAuthentication'
        ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer'
    ]
}

AUTHENTICATION_BACKEND = ['django.contrib.auth.backends.ModelBackend']


GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")



CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv("CLOUD_NAME"),
    'API_KEY': os.getenv("API_KEY"),
    'API_SECRET': os.getenv("API_SECRET")
}
