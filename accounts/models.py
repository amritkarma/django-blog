from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.conf import settings


from PIL import Image
from accounts.utils import get_user_initial


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(
        max_length=225, verbose_name='Email', unique=True, db_index=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True, validators=[RegexValidator(regex=r'^\d{10}$', message='Enter a valid 10-digit phone number')]
)
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


def upload_profile_image(instance, filename, **kwargs):
    file_name = f'Profile/{instance.user.username}/{filename}'
    return file_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True)
    slug = models.SlugField(max_length=225, unique=True, blank=True)
    profile_image = models.ImageField(
        upload_to=upload_profile_image, blank=True, null=True)
    bio = models.TextField(max_length=225, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.profile_image:
            profileimage = Image.open(self.profile_image.file)

            if profileimage.height > 400 or profileimage.width > 400:
                size = (400, 400)
                profileimage.thumbnail(size, Image.Resampling.LANCZOS)
                profileimage.save(self.profile_image.path,
                                  quality=96, optimize=True)
    
    @property
    def placeholder_initial(self):
        return get_user_initial(self.user)

    def get_absolute_url(self):
        return reverse('auth:profile', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Profiles'