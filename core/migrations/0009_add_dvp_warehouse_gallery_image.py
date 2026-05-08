"""Data migration: add 'ДВП Деревоволокниста плита' photo to gallery."""
from django.db import migrations


def add_dvp_image(apps, schema_editor):
    GalleryImage = apps.get_model("core", "GalleryImage")
    GalleryImage.objects.get_or_create(
        image_static="img/gallery/dvp-warehouse.png",
        defaults={
            "alt_text": "ДВП деревоволокниста плита — стопки на піддонах у складі",
            "caption": "ДВП Деревоволокниста плита",
            "lightbox_caption": "ДВП — деревоволокниста плита на складі",
            "badge_label": "ДВП",
            "badge_colour": "amber",
            "order": 14,
            "is_visible": True,
        },
    )


def remove_dvp_image(apps, schema_editor):
    GalleryImage = apps.get_model("core", "GalleryImage")
    GalleryImage.objects.filter(image_static="img/gallery/dvp-warehouse.png").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_add_fk_warehouse_gallery_image"),
    ]

    operations = [
        migrations.RunPython(add_dvp_image, remove_dvp_image),
    ]
