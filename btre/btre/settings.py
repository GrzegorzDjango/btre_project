"""
Django settings for btre project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3c%i^*l3y64ifpouvypy7(de5^zbd_ui!6!7wfrom8=tn=(978'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# dodajemy odwołanie do każdej apki którą stworzyliśmy '<nazwa app>.apps.<nazwa klasy w pliku apps.py>'
INSTALLED_APPS = [
    'contacts.apps.ContactsConfig',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', #dodajemy żeby móc formatować cenę nieruchomości w listings.html
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# zaczyna szukać url od pliku urls.py w folderze btre
ROOT_URLCONF = 'btre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # w tym folderze zaczynamy odniesienia np. {% url 'accounts/dashboard.html' %} co znaczy ze w folderze templates jest foler accounts i w nim dashboard.html
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'btre.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # baza danych gdzie będą zapisani użytkownicy i dane do modeli, Django zajmuje się SQLem itp
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btredb',
        'USER': 'postgres',
        'PASSWORD': 'abc123',
        'HOST': '',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#collectstatic tutaj da wszystkie statici
#python manage.py collectstatic stworzy folder static w roocie (równolegle do folderu projektu btre i templates
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#lokacja folderu staticfiles gdzie są css, img, javascripty i obrazki :
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'btre/static')
]

#Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#messages ustawianie wiadomości które my akurat chcemy wyświetlaś przy rejestracji, logowaniu itp gdzie może pojawić się np. błąd
#to podspodem bierzemy z dokumentacji
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# ustawiamy email, nie zadziałało bo google zblokowało
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'grzegorz.kania1983@gmail.com'
EMAIL_HOST_PASSWORD = 'tajnehasło!'
EMAIL_USE_TLS = True