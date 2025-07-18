from django.db import models
from django.urls import reverse

from accounts.models import User

# Create your models here.

def upload_posts_image(instance, filename, **kwargs):
    file_name = f'posts/{filename}'
    return file_name


class Post(models.Model):
    class StatusChoice(models.TextChoices):
        Publish = 'Publish'
        Draft = 'Draft'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,)
    seo_title = models.CharField(max_length=2000,  blank=True, null=True)
    seo_description = models.TextField(max_length=2000,  blank=True, null=True)
    slug = models.SlugField(max_length=2000, unique=True)
    category = models.ForeignKey('PostCategory', on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.Publish)
    image = models.ImageField(upload_to=upload_posts_image, blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('posts:postdetail', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["created"]
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class PostCategory(models.Model):
    name = models.CharField(max_length=255,)
    slug = models.SlugField(max_length=2000, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self) -> str:
        return reverse('posts:categorydetail', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["created"]
        verbose_name = 'Post Category'
        verbose_name_plural = 'Posts Categories'

class PostComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE)
    comment = models.TextField(max_length=2000,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Comment by {self.user} on {self.post}'

    class Meta:
        ordering = ["created"]
        verbose_name = 'Post Comment'
        verbose_name_plural = 'Posts Comments'

class Contact(models.Model):
    name = models.CharField(max_length=255,)
    email = models.EmailField(max_length=255,)
    message = models.TextField(max_length=2000,)
    created = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(protocol='both', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        ordering = ['created']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class Subscribe(models.Model):
    name = models.CharField(max_length=255,)
    email = models.EmailField(max_length=255, unique=True)
    ip_address = models.GenericIPAddressField(protocol='both', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        ordering = ['created']
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'

class RobotsTxt(models.Model):
    title = models.CharField(max_length=2000, blank=True, null=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        ordering = ['created']
        verbose_name = 'Robots Txt'
        verbose_name_plural = 'Robots Txts'

class AdsTxt(models.Model):
    title = models.CharField(max_length=2000, blank=True, null=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        ordering = ['created']
        verbose_name = 'Ads Txt'
        verbose_name_plural = 'Ads Txts'

