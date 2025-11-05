###########################
# core/settings/test.py
###########################
"""
Configurações para ambiente de TESTES.
"""

from .base import *

# -----------------------------------------------------------------------------
# Segurança
# -----------------------------------------------------------------------------
DEBUG = False
SECRET_KEY = "test-key-not-secure-q#o-!3u#z$4!*upt@!$xs=f@p7&8qn"
ALLOWED_HOSTS = ["*"]

# Desativa recursos de segurança para testes
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# -----------------------------------------------------------------------------
# Banco de dados
# -----------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# -----------------------------------------------------------------------------
# Cache
# -----------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# -----------------------------------------------------------------------------
# Middleware
# -----------------------------------------------------------------------------
# Remove middleware não necessário em testes
MIDDLEWARE = [
    m for m in MIDDLEWARE 
    if m not in [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
    ]
]

# -----------------------------------------------------------------------------
# Apps
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    app for app in INSTALLED_APPS 
    if app not in [
        "debug_toolbar",
        "whitenoise.runserver_nostatic",
    ]
]