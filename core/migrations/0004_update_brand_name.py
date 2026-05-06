from django.db import migrations


def update_header_name(apps, schema_editor):
    SiteSettings = apps.get_model("core", "SiteSettings")
    SiteSettings.objects.filter(pk=1).update(header_name="ФАНЕРА  ДВП")


def revert_header_name(apps, schema_editor):
    SiteSettings = apps.get_model("core", "SiteSettings")
    SiteSettings.objects.filter(pk=1).update(header_name="ФОП Музичко М.В.")


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_seed_cms_data"),
    ]

    operations = [
        migrations.RunPython(update_header_name, revert_header_name),
    ]
