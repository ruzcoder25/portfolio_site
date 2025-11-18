"""
Django settings for port project.
Deploy-ready configuration for Render.com
"""

import os
from pathlib import Path
from decouple import config
import dj_database_url

# =====================================
#     ASOSIY PATHLAR
# =====================================
BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================
#     XAVFSIZLIK
# =====================================
SECRET_KEY = config('SECRET_KEY', default='changeme-in-prod')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.onrender.com',    # Render domeni
    'ruzcoder.uz',     # O'z domeningiz
]

# =====================================
#     INSTALLED APPS
# =====================================
INSTALLED_APPS = [
    # Django default app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # WhiteNoise (statik fayllar uchun)
    'whitenoise.runserver_nostatic',

    # Lokal app'lar
    'account',
    'education',
    'language',
    'projects',
    'skill',
    'port_view',
    'dashboard',
]

# =====================================
#     MIDDLEWARE
# =====================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static fayllar
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'port.urls'

# =====================================
#     TEMPLATES
# =====================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'port.wsgi.application'

# =====================================
#     DATABASE
# =====================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='portfolio_db'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default='postgres'),
        'HOST': config('DB_HOST', default='127.0.0.1'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Agar DATABASE_URL ishlatilsa (Render.com uchun)
db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)

# =====================================
#     PASSWORD VALIDATION
# =====================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =====================================
#     LOKAL VA VAQT
# =====================================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

# =====================================
#     STATIC & MEDIA
# =====================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =====================================
#     CUSTOM USER & LOGIN
# =====================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'account.CustomUser'
LOGIN_URL = '/accounts/login_admin/'

# =====================================
#     DJANGO REST FRAMEWORK
# =====================================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# =====================================
#     SESSION SETTINGS
# =====================================
SESSION_COOKIE_AGE = 300  # 5 daqiqa
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# =====================================
#     HTTPS (Render.com uchun)
# =====================================
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://ruzcoder.uz',
]
