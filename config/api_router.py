from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from corpsystem_teste.app.modules.users.api.views import UserViewSet
from corpsystem_teste.app.modules.clients.api.views import ClientsViewSet
from corpsystem_teste.app.modules.sellers.api.views import SellersViewSet
from corpsystem_teste.app.modules.products.api.views import ProductsViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("products", ProductsViewSet, basename="products")
router.register("clients", ClientsViewSet, basename="clients")
router.register("sellers", SellersViewSet, basename="sellers")


app_name = "api"
urlpatterns = router.urls
