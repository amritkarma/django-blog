from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.contrib.syndication.views import Feed
from posts.feed import PostFeed


from posts.views import (
    HomePageView,
    AdstxtView,
    CategoryDetailView,
    ContactView,
    PostsView,
    PostDetailView,
    PrivacyPolicyView,
    RobotstxtView,
    SubScribeView,
)
from posts.sitemaps import PostViewSitemap


app_name = "posts"

sitemaps_posts = {
    "static": PostViewSitemap,
}

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("posts/", PostsView.as_view(), name="posts"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("subscribe/", SubScribeView.as_view(), name="subscribe"),
    path("privacy/", PrivacyPolicyView.as_view(), name="privacy"),
    path("rss/", PostFeed(), name="rss"),
    path("category/<slug:slug>/",
         CategoryDetailView.as_view(),
         name="categorydetail"
         ),
    path("<slug:slug>/", PostDetailView.as_view(), name="postdetail"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps_posts},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("ads.txt", AdstxtView.as_view(), name="ads.txt"),
    path("robots.txt", RobotstxtView.as_view(), name="robots.txt"),
]
