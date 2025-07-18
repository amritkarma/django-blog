from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from posts.models import Post


class PostFeed(Feed):
    title = "Your Blog Title"
    link = "/rss/"
    description = "Latest posts from Your Blog"

    def items(self):
        return Post.objects.filter(status='Publish').order_by('-created')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.description, 30)

    def item_link(self, item):
        return reverse('posts:postdetail', args=[item.slug])
