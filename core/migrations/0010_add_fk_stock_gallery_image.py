"""Data migration: add 'Фанера на складі' photo to gallery."""
from django.db import migrations


def add_fk_stock_image(apps, schema_editor):
    GalleryImage = apps.get_model("core", "GalleryImage")
    GalleryImage.objects.get_or_create(
        image_static="img/gallery/fk-stock.png",
        defaults={
            "alt_text": "Фанера клеєна ФК на складі — стопки листів різної товщини та сортності",
            "caption": "Фанера на складі",
            "lightbox_caption": "Фанера клеєна ФК — асортимент на складі",
            "badge_label": "ФК",
            "badge_colour": "green",
            "order": 15,
            "is_visible": True,
        },
    )


def remove_fk_stock_image(apps, schema_editor):
    GalleryImage = apps.get_model("core", "GalleryImage")
    GalleryImage.objects.filter(image_static="img/gallery/fk-stock.png").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_add_dvp_warehouse_gallery_image"),
    ]

    operations = [
        migrations.RunPython(add_fk_stock_image, remove_fk_stock_image),
    ]
