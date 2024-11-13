"""
Django settings for AbsensiMahasiswa project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0m0g0ye0abxf)pijsbx7e_0jz(c%=oqs=2e$g%%ch&p3tkd8g&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "feedback",
    "HistoriKehadiran",
    "Master",
    "UserProfile",
    "KRS",
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

ROOT_URLCONF = 'AbsensiMahasiswa.urls'

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

WSGI_APPLICATION = 'AbsensiMahasiswa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "AbsensiMahasiswa",
        "USER": "postgres",
        "PASSWORD": "neekaru2118",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

UNFOLD = {
    "SITE_TITLE": "Sistem Absensi Mahasiswa",
    "SITE_HEADER": "SIAM",
    # "SITE_ICON": {
    #     "light": lambda request: static("logo_poltek.png"),  # light mode
    #     "dark": lambda request: static("logo_poltek.png"),  # dark mode
    # }
    "SITE_SYMBOL": "school",  # symbol from icon set
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
    "SIDEBAR": {
        "show_search": False,  # Search in applications and models names
        "show_all_applications": False,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Navigation"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",  # Supported icon set: https://fonts.google.com/icons
                        "link": reverse_lazy("admin:index"),
                        "permission": lambda request: request.user.is_superuser,
                        "group": "admin",
                    },
                ],
            },
            {
                "title": _("Master Data"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Mahasiswa"),
                        "icon": "person",
                        "link": reverse_lazy("admin:Master_mahasiswa_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                        "group": "master",
                    },
                    {
                        "title": _("Dosen"),
                        "icon": "business",
                        "link": reverse_lazy("admin:Master_dosen_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                        "group": "master",
                    },
                    {
                        "title": _("Mata Kuliah"),
                        "icon": "book",
                        "link": reverse_lazy("admin:Master_matakuliah_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                        "group": "master",
                    },
                ],
            },
            {
                "title": _("Data Histori Kehadiran"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("Histori Kehadiran"),
                        "icon": "history_edu",
                        "link": reverse_lazy("admin:HistoriKehadiran_historikehadiran_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                        "group": "historikehadiran",
                    },
                ],
            },
            {
                "title": _("Data KRS"),
                "separator": True,  # Top border
                "collapsible": True,  # Collapsible group of links
                "items": [
                    {
                        "title": _("KRS"),
                        "icon": "list_alt",
                        "link": reverse_lazy("admin:KRS_krs_changelist"),
                        "permission": lambda request: request.user.is_superuser,
                        "group": "krs",
                    },
                ],
            },
        ],
    },
}