import os
import django_heroku
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.getenv('DJANGO_USER_SECRET_KEY')
SECRET_KEY = os.environ.get('DJANGO_USER_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8000',
)

ALLOWED_HOSTS = ['https://secret-meadow-84520.herokuapp.com', 'http://127.0.0.1:8000',]

AUTH_USER_MODEL = 'accounts.CustomUser'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', #new
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    
    'bootstrap4',
    'bootstrap_datepicker_plus',

    'accounts',

]



MIDDLEWARE = [
    # 'customuser_project.tzonemiddleware.TimezoneMiddleware', # New middleware
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # New
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'customuser_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')), ],
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


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # New
    ],
}


WSGI_APPLICATION = 'customuser_project.wsgi.application'

BOOTSTRAP4 = { 'include_jquery': True }

SECURE_HSTS_SECONDS=3600 
SESSION_COOKIE_SECURE=True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
SECURE_HSTS_PRELOAD=True
SECURE_SSL_REDIRECT=True
SECURE_HSTS_INCLUDE_SUBDOMAINS=True

CORS_ORIGIN_ALLOW_ALL = True

#DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
#EMAIL_HOST = os.getenv('EMAIL_HOST')
#EMAIL_HOST_USER = os.getenv('SENDGRID_USER') # new
#EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_PASSWORD')
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#EMAIL_USE_SSL = False

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('am', _('Amharic')),
    ('en', _('English')),
    ('om', _('Afaan Oromoo')),
    #('de', _('German')),
    #('fr', _('French')),
    #('es', _('Spanish')),
    #('pt', _('Portuguese'))
    #('ru', _('Russian')),
    ('zh-Hans', _('Simplified Chinese')),
]

TIME_ZONE = 'UTC'
USE_TZ = True

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'
LOGIN_URL = 'accounts:log_in'

ENABLE_USER_ACTIVATION = True
DISABLE_USERNAME = False
LOGIN_VIA_EMAIL = False
LOGIN_VIA_EMAIL_OR_USERNAME = True
USE_REMEMBER_ME = False

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = True
EMAIL_ACTIVATION_AFTER_CHANGING = True
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True

SIGN_UP_FIELDS = ['username', 'email', 'mobile_phone', 'password1', 'password2']
if DISABLE_USERNAME:
    SIGN_UP_FIELDS = ['email', 'mobile_phone', 'password1', 'password2']

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

THOUSAND_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_ROOT = os.path.join(BASE_DIR, '/static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'),]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Activate Django-Heroku.
django_heroku.settings(locals())