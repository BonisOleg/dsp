"""Data migration: add 'ФК Фанера клеєна 1525х1525' photo to gallery."""
from django.db import migrations


def add_warehouse_image(apps, schema_editor):
    GalleryImage = apps.get_model("core", "GalleryImage")
    GalleryImage.objects.get_or_create(
        image_static="img/gallery/fk-warehouse-1525.png",
        defaults={
            "alt_text": "Фанера клеєна ФК 1525х1525 — стопки на складі з маркуванням товщини та сортності",
            "caption": "ФК Фанера клеєна 1525х1525",
            "lightbox_caption": "Фанера клеєна ФК 1525х1525 — різні товщини та сортність",
            "badge_label": "ФК",
            "badge_colour": "green",
            "order": 13,
            "is_visible": True,
        },
    )


def remove_warehouse_image(apps, schema_editor):
    GalleryImage = apps.get_model("core", "GalleryImage")
    GalleryImage.objects.filter(image_static="img/gallery/fk-warehouse-1525.png").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_add_delivery_gallery_image"),
    ]

    operations = [
        migrations.RunPython(add_warehouse_image, remove_warehouse_image),
    ]
