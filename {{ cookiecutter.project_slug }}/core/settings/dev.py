###########################
# core/settings/dev.py
###########################
"""
Configurações para ambiente de DESENVOLVIMENTO.
"""

from .base import *

# -----------------------------------------------------------------------------
# Segurança
# -----------------------------------------------------------------------------
DEBUG = True
ALLOWED_HOSTS = ["*"]

# -----------------------------------------------------------------------------
# Banco de dados local (SQLite)
# -----------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
