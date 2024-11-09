import os
from pathlib import Path

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'your-secret-key'  # Replace with your actual secret key
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ['127.0.0.1', 'project-62-3.onrender.com']  # Allowed hosts for production and development

# Installed apps including your app 'portfolio'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',  # Your app
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'Project_62_3.urls'

# Template settings, with directory pointing to 'templates' folder in the main project directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Main templates directory
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

# WSGI application for production
WSGI_APPLICATION = 'Project_62_3.wsgi.application'

# Database settings (SQLite for now, change to PostgreSQL or MySQL in production if needed)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'

# Where to store static files when deploying
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Update STATICFILES_DIRS to point to the 'static' directory in 'portfolio'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]



# Media files settings (optional, if you’re using uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Password validation settings
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

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Additional settings you may need to update or add:
# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Locale paths
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# Enable CSRF protection (which is by default enabled)
CSRF_COOKIE_SECURE = False  # Change to True in production

# Session settings
SESSION_COOKIE_SECURE = False  # Change to True in production

