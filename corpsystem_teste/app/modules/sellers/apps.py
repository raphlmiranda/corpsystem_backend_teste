from django.apps import AppConfig


class SellersConfig(AppConfig):
    name = "corpsystem_teste.app.modules.sellers"
    verbose_name = "sellers"

    def ready(self):
        try:
            import corpsystem_teste.app.modules.sellers.signals  # noqa F401
        except ImportError:
            pass
