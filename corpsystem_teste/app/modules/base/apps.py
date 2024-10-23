from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = "corpsystem_teste.app.modules.base"
    verbose_name = "base"

    def ready(self):
        try:
            import corpsystem_teste.app.modules.base.signals  # noqa F401
        except ImportError:
            pass
