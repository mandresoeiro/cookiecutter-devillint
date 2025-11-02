#!/usr/bin/env python
"""Gerenciador principal de comandos Django no projeto."""

import os
import sys
from decouple import config


def main():
    """Configura o DJANGO_SETTINGS_MODULE com suporte ao .env."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        config("DJANGO_SETTINGS_MODULE", default="core.settings.dev")
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django não está instalado.") from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
