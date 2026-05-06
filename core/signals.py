"""Post-delete signals: clean up uploaded media files when model instances are removed."""
import logging

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from .models import GalleryImage, Product

logger = logging.getLogger(__name__)


def _delete_file(field):
    """Delete a FieldFile from storage, swallowing errors so a failed cleanup never breaks a request."""
    if not field:
        return
    try:
        storage = field.storage
        if storage.exists(field.name):
            storage.delete(field.name)
    except Exception:
        logger.exception("Could not delete media file: %s", field.name)


# ── GalleryImage ─────────────────────────────────────────────────────────────

@receiver(post_delete, sender=GalleryImage)
def gallery_image_post_delete(sender, instance, **kwargs):
    _delete_file(instance.image)


@receiver(pre_save, sender=GalleryImage)
def gallery_image_pre_save(sender, instance, **kwargs):
    """When an image is replaced, delete the old file from storage."""
    if not instance.pk:
        return
    try:
        old = GalleryImage.objects.get(pk=instance.pk)
    except GalleryImage.DoesNotExist:
        return
    if old.image and old.image != instance.image:
        _delete_file(old.image)


# ── Product ───────────────────────────────────────────────────────────────────

@receiver(post_delete, sender=Product)
def product_post_delete(sender, instance, **kwargs):
    _delete_file(instance.image)


@receiver(pre_save, sender=Product)
def product_pre_save(sender, instance, **kwargs):
    """When an image is replaced, delete the old file from storage."""
    if not instance.pk:
        return
    try:
        old = Product.objects.get(pk=instance.pk)
    except Product.DoesNotExist:
        return
    if old.image and old.image != instance.image:
        _delete_file(old.image)
