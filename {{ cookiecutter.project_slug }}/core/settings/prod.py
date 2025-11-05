# settings prod.py exemplo
###########################
# core/settings/prod.py
###########################
"""
Configurações para ambiente de PRODUÇÃO.
Requer variáveis sensíveis definidas em .env
"""

from .base import *
from decouple import config

# -----------------------------------------------------------------------------
# Segurança
# -----------------------------------------------------------------------------
DEBUG = False
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="").split(",")

# -----------------------------------------------------------------------------
# Banco de dados PostgreSQL
# -----------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB", default="movies_db"),
        "USER": config("POSTGRES_USER", default="movies_user"),
        "PASSWORD": config("POSTGRES_PASSWORD", default="unsafe"),
        "HOST": config("POSTGRES_HOST", default="localhost"),
        "PORT": config("POSTGRES_PORT", default="5432"),
    }
}
