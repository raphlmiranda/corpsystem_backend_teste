from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = "corpsystem_teste.app.modules.products"
    verbose_name = "products"

    def ready(self):
        try:
            import corpsystem_teste.app.modules.products.signals  # noqa F401
        except ImportError:
            pass
