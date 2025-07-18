from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


from accounts.models import Profile

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def profile_save(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance, slug=slugify(instance.username))
