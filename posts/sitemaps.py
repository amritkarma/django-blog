from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from posts.models import Post


class PostViewSitemap(Sitemap):
    priority = '0.4'
    changefreq = 'daily'

    def items(self):
        return Post.objects.filter(status='Publish').order_by('-created')

    def lastmod(self, obj):
        return obj.created
