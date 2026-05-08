"""Data migration: add 'Фанера — можлива доставка' photo to gallery."""
from django.db import migrations


def add_delivery_image(apps, schema_editor):
    GalleryImage = apps.get_model("core", "GalleryImage")
    GalleryImage.objects.get_or_create(
        image_static="img/gallery/fk-delivery.png",
        defaults={
            "alt_text": "Фанера ФК завантажена у вантажівку — можлива доставка",
            "caption": "Фанера — можлива доставка",
            "lightbox_caption": "Фанера ФК — відвантаження, можлива доставка по регіону",
            "badge_label": "ФК",
            "badge_colour": "green",
            "order": 12,
            "is_visible": True,
        },
    )


def remove_delivery_image(apps, schema_editor):
    GalleryImage = apps.get_model("core", "GalleryImage")
    GalleryImage.objects.filter(image_static="img/gallery/fk-delivery.png").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_sitesettings_ui_labels"),
    ]

    operations = [
        migrations.RunPython(add_delivery_image, remove_delivery_image),
    ]
