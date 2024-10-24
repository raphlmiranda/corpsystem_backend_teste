# ruff: noqa
from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from corpsystem_teste.app.modules.sales.api.views import export_file

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]

# API URLS
urlpatterns += [
    # DRF auth token
    path("api/sales/export/", export_file, name="sales-export"),
    path("api/", include("config.api_router")),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]
