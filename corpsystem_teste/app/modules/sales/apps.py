from django.apps import AppConfig


class SalesConfig(AppConfig):
    name = "corpsystem_teste.app.modules.sales"
    verbose_name = "sales"

    def ready(self):
        try:
            import corpsystem_teste.app.modules.sales.signals  # noqa F401
        except ImportError:
            pass
