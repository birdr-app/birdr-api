"""
Django settings for  project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'testing-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',    
]


# Application definition

INSTALLED_APPS = [
    'daphne',
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
    'birdr'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'birdr.urls'

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

WSGI_APPLICATION = 'birdr.wsgi.application'
ASGI_APPLICATION = "birdr.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'django/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.apple.AppleIdAuth',
    'django.contrib.auth.backends.ModelBackend',
)

# Social OAuth2 settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<YOUR_GOOGLE_CLIENT_ID>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<YOUR_GOOGLE_CLIENT_SECRET>'

SOCIAL_AUTH_APPLE_ID_CLIENT = '<YOUR_APPLE_CLIENT_ID>'
SOCIAL_AUTH_APPLE_ID_SECRET = '<YOUR_APPLE_SECRET>'

SOCIAL_AUTH_AZUREAD_OAUTH2_KEY = '<YOUR_MICROSOFT_CLIENT_ID>'
SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET = '<YOUR_MICROSOFT_SECRET>'
SOCIAL_AUTH_AZUREAD_TENANT_ID = '<YOUR_MICROSOFT_TENANT_ID>'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
   'DEFAULT_FILTER_BACKENDS': [
       'rest_framework.filters.OrderingFilter'
   ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=4),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1000),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<YOUR_GOOGLE_CLIENT_ID>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<YOUR_GOOGLE_CLIENT_SECRET>'
SOCIAL_AUTH_APPLE_ID_CLIENT = '<YOUR_APPLE_CLIENT_ID>'
SOCIAL_AUTH_APPLE_ID_SECRET = '<YOUR_APPLE_CLIENT_SECRET>'
SOCIAL_AUTH_AZUREAD_OAUTH2_KEY = '<YOUR_MICROSOFT_CLIENT_ID>'
SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET = '<YOUR_MICROSOFT_CLIENT_SECRET>'
SOCIAL_AUTH_AZUREAD_TENANT_ID = '<YOUR_TENANT_ID>'

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://localhost:3000/login/google'

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://.be",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = ["GET", "POST", "OPTIONS", "PUT", "DELETE"]
CORS_ALLOW_HEADERS = ["*"]

SECURE_CROSS_ORIGIN_OPENER_POLICY = None
SECURE_CROSS_ORIGIN_EMBEDDER_POLICY = None
# SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"