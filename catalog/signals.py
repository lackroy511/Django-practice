from django.db.models.signals import pre_save
from django.dispatch import receiver
from catalog.models import Version


@receiver(pre_save, sender=Version)
def ensure_single_active_version(sender, instance, **kwargs):
    if instance.version_is_active:
        # Если текущая версия является активной, отключите все другие активные версии для этого продукта
        Version.objects.filter(product=instance.product, version_is_active=True).exclude(pk=instance.pk).update(version_is_active=False)