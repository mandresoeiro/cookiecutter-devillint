from django.apps import AppConfig

class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
    verbose_name = 'Dashboard'

    def ready(self):
        """
        Inicialização do app
        """
        try:
            import dashboard.signals  # noqa
        except ImportError:
            pass