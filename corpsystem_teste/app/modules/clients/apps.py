from django.apps import AppConfig


class ClientsConfig(AppConfig):
    name = "corpsystem_teste.app.modules.clients"
    verbose_name = "clients"

    def ready(self):
        try:
            import corpsystem_teste.app.modules.clients.signals  # noqa F401
        except ImportError:
            pass
