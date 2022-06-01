"""
Django settings for SMS project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from django.contrib.messages import constants as messages
import os
import moneyed
from moneyed.localization import _FORMATTER
from decimal import ROUND_HALF_EVEN
#from easy_thumbnails.conf import Settings as thumbnail_settings


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# images directory
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
#with open('/etc/talents/secret_key.txt') as f:
    #SECRET_KEY = f.read().strip()
SECRET_KEY = 'iipz_!e!h^%8w3ghn)lbnutxv$sht&ynz)uvy&vq!6v2&h1nfi'

#with open('/etc/talents/database_password.txt') as f:
#    DATABASE_PASSWORD = f.read().strip()




MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['talents.esi.dz']
PROTOCOLE_HOST = 'http://localhost:8000'
# EMAIL
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'talents@esi.dz'
#with open('/etc/talents/email_host_password.txt') as f:
 #   EMAIL_HOST_PASSWORD = f.read().strip()
EMAIL_PORT = 587

# EMAIL_ENABLED = True to activate sending emails
EMAIL_ENABLED = False
STAFF_EMAILS = {
    'scolarite':['scolarite@esi.dz'],
    'direction':['n_cherid@esi.dz'],
    'stage':['y_challal@esi.dz'],
    'futurs_stagiaires':['y_challal@esi.dz'],
    'webmaster':['y_challal@esi.dz'],
    #'stage':['d_ait_ali_yahia@esi.dz']
}

# google AGENA parametes
SCOPES=["https://www.googleapis.com/auth/calendar"]
GOOGLE_CLIENT_SECRET_FILE="/etc/talents/code_secret_client_fet.json"

# SMS PROVIDER SETTINGS
SMS_ENABLED=False
SMS_URL='https://wsp.sms-algerie.com/api/json'
SMS_API_KEY='00baa5ee9bf52576a0deaf2b6d800b83f682f77f'
SMS_USER_KEY='2230321e5902f6072a0337ef06034889'

# Application definition
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
INSTALLED_APPS = [
    'scolar.apps.ScolarConfig',
    'django_tables2',
    'django_filters',
    'crispy_forms',
    'jquery',
    'bootstrap4',
    'bootstrap_datepicker_plus',
    'social_django',
    'jchart',
    'django_icons',
    'wkhtmltopdf',
    'django_ajax',
    'django_select2',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'djmoney',
    'mathfilters',

]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 86400 # sec
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_NAME = 'DSESSIONID'
SESSION_COOKIE_SECURE = False
DATE_INPUT_FORMATS = ['%d/%m/%Y']
CRISPY_TEMPLATE_PACK = 'bootstrap4'

TIME_INPUT_FORMATS = ['%I:%M %p']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'SMS.urls'

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
                'django.template.context_processors.i18n',
                'social_django.context_processors.backends',    # social_django
                'social_django.context_processors.login_redirect', # social_django 
                'scolar.context_processors.institution', # default context institution info
            ],
        },
    },
]

BOOTSTRAP4 = {
    'include_jquery': True,
}

WSGI_APPLICATION = 'SMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ATOMIC_REQUESTS':True,
    }
}

# Login
LOGIN_URL = '/accounts/login'
LOGOUT_REDIRECT_URL = '/scolar/index'
LOGIN_REDIRECT_URL = '/scolar/index'

AUTH_USER_MODEL = 'scolar.User'

AUTHENTICATION_BACKENDS = (     # enable authentication against two backends Google and Model
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# social django features and auth strategy
SOCIAL_AUTH_PIPELINE = (    
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
SOCIAL_AUTH_STRATEGY = 'social_django.strategy.DjangoStrategy'  # new
SOCIAL_AUTH_STORAGE = 'social_django.models.DjangoStorage'  # new
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '788698204337-hf38104m1m42tte4t87aoklf29uedl82.apps.googleusercontent.com' # new
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'qWHKbQlOynagtGQarIZ2mdhn'   # new


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'Africa/Algiers'

USE_I18N = True

USE_L10N = True   # pr afficher suffix de dzd

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'root') 
STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]

WKHTMLTOPDF_CMD_OPTIONS = {
   'enable-local-file-access': True,
}
# security settings
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
#SECURE_HSTS_SECONDS = 3600
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_SSL_HOST = 'talents.esi.dz'
#SECURE_SSL_REDIRECT = True
#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_BROWSER_XSS_FILTER = True
#X_FRAME_OPTIONS = 'SAMEORIGIN'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
