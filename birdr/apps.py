from django.apps import AppConfig

class BirdrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'birdr'

    def ready(self):
        from .signals import create_initial_country_game  # noqa 