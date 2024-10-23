"""Modify version from cookie cutter to work with MySQL8.3."""
from django.conf import settings
from django.db import migrations


def update_or_create_site(apps, schema_editor, domain, name):
    """Update or create the site with the specified domain and name."""
    Site = apps.get_model("sites", "Site")
    Site.objects.update_or_create(
        id=settings.SITE_ID,
        defaults={
            "domain": domain,
            "name": name,
        },
    )

def update_site_forward(apps, schema_editor):
    """Set site domain and name."""
    update_or_create_site(
        apps,
        schema_editor.connection,
        "elcolie.co.th",
        "elcolie",
    )


def update_site_backward(apps, schema_editor):
    """Revert site domain and name to default."""
    update_or_create_site(
        apps,
        schema_editor.connection,
        "example.com",
        "example.com",
    )


class Migration(migrations.Migration):

    dependencies = [("sites", "0002_alter_domain_unique")]

    operations = [migrations.RunPython(update_site_forward, update_site_backward)]