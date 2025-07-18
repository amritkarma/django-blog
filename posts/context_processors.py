import os
from posts.models import PostCategory

def categories_processor(request):
    categories = PostCategory.objects.all().order_by("name")
    return {'post_categories': categories}

HOST_DOMAIN_URL = os.getenv("HOST_DOMAIN_URL")
print(HOST_DOMAIN_URL)

def host_domain_url(request):
    return {'HOST_DOMAIN_URL': HOST_DOMAIN_URL}
