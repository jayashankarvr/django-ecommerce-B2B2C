"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import mimetypes

mimetypes.add_type("text/javascript", ".js", True)
mimetypes.add_type("text/css", ".css", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dr&-v@o7w9#&#r3wj$d#$t78t&*hb$&(2)xa5@05d1p$)1=$96'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]

STRIPE_PUB_KEY = 'pk_test_51Ikdb4HwFojfx57irEolkyNAWZCsGCRlrBEKIt4WZXhOTg25Lw50WpUFY5OmDb504spl1XcnaQlswKQu0ULBkpbD003XV2jNJt'
STRIPE_SECRET_KEY = 'sk_test_51Ikdb4HwFojfx57ik70ouFvnOA2MWIE2QqZkcCmB3yO142YvuuLWc4pSBkI5yDT4y77a9oDq6NWWYXxNtGn52A3700yNZd411N'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'vendor_admin'
LOGOUT_REDIRECT_URL = 'frontpage'

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'
COUPON_SESSION_ID = 'coupon'
SESSION_SAVE_EVERY_REQUEST = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'warehouse2fifty@gmail.com'
EMAIL_HOST_PASSWORD = 'Warehousedistrict2021'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_EMAIL_FROM = ''

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'djrichtextfield',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    # 'django_markdown',
    'ckeditor',
    'ckeditor_uploader',

    'apps.cart',
    'apps.core',
    'apps.newsletter',
    'apps.order',
    'apps.product',
    'apps.vendor',
    'apps.blog',
    'apps.dashboard',
    'apps.coupon',
    'apps.newProduct',
    'apps.home',
    'apps.transporter',
    'apps.ordering',
    'apps.maintenance',


    # 'rest_framework',
    'widget_tweaks',
    'crispy_forms',
    'mathfilters',
    'bootstrap4',
    'django_addanother',
    'django_select2',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.maintenance.middleware.UnderConstructionMiddleware',
]


ROOT_URLCONF = 'main.urls'

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
                'apps.product.context_processors.menu_categories',
                'apps.cart.context_processors.cart',
                'apps.cart.context_processors.comparing',
            ],
        },
    },
]

UNDER_CONSTRUCTION = False


WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Kigali'

USE_I18N = True

USE_L10N = True

USE_TZ = False

USE_THOUSAND_SEPARATOR = True
SESSION_SAVE_EVERY_REQUEST = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apps/dashboard/static'),
]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)

# RELATIVES_CACHE_KEY = 'relatives_cache'
# RELATIVES_CACHE_TIME = int(60*60*24)


STATIC_ROOT = os.path.join(BASE_DIR, "static")


# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(CORE_DIR, 'core/static'),
# )


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
CKEDITOR_UPLOAD_PATH = 'images/'
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"

# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
