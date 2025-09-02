import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.db.models import Q

from posts.models import Contact, Post, PostCategory, PostComments, Subscribe
from posts.forms import ContactForm, PostCommentsForm, SubscribeForm
from posts.utils import get_ip_address

# Create your views here.


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        featured_post = Post.objects.filter(status="Publish").order_by("-created").first()
        recent_posts = Post.objects.filter(status="Publish")

        if featured_post:
            recent_posts = recent_posts.exclude(id=featured_post.id)

        recent_posts = recent_posts.order_by("-created")[:6]

        context["featured_post"] = featured_post
        context["recent_posts"] = recent_posts

        return context


class PostsView(ListView):
    model = Post
    template_name = "posts/posts.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search", "")
        context["search"] = search
        context["no_results"] = search and not self.get_queryset().exists()
        return context

    def get_queryset(self):
        queryset = super().get_queryset().filter(status="Publish").order_by("-created")
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(title__contains=search) | Q(slug__contains=search)
            )
            return queryset
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/postdetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object.status == "Draft" and not self.object.user == self.request.user:
            raise Http404

        comments = (
            PostComments.objects.filter(post=self.object, parent__isnull=True)
            .select_related("user")
            .prefetch_related("replies")
        )

        previous_post = (
            Post.objects.filter(status="Publish", created__lt=self.object.created)
            .order_by("-created")
            .first()
        )

        next_post = (
            Post.objects.filter(status="Publish", created__gt=self.object.created)
            .order_by("created")
            .first()
        )

        related_posts = []
        if self.object.category:
            related_posts = (
                Post.objects.filter(
                    category=self.object.category, status=Post.StatusChoice.Publish
                )
                .exclude(pk=self.object.pk)
                .order_by("-created")[:4]
            )

        context["comment_form"] = PostCommentsForm()
        context["comments"] = comments
        context["related_posts"] = related_posts
        context["previous_post"] = previous_post
        context["next_post"] = next_post
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = PostCommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.object

            parent_id = request.POST.get("parent_id")
            if parent_id:
                try:
                    parent_comment = PostComments.objects.get(id=parent_id)
                    comment.parent = parent_comment
                except PostComments.DoesNotExist:
                    pass  # fallback to top-level comment if invalid parent

            comment.save()
            return redirect(self.object.get_absolute_url())
        else:
            # Return with errors and current context
            context = self.get_context_data()
            context["comment_form"] = form
            return self.render_to_response(context)


class CategoryDetailView(DetailView, MultipleObjectMixin):
    model = PostCategory
    template_name = "posts/categorydetail.html"
    context_object_name = "category"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        object_list = Post.objects.filter(
            category=self.object, status=Post.StatusChoice.Publish
        ).order_by("-created")
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class ContactView(SuccessMessageMixin, FormView):
    model = Contact
    form_class = ContactForm
    template_name = "posts/contact.html"
    success_url = reverse_lazy("posts:contact")
    success_message = "Message Sent Succecssfull!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        instance = form.save(commit=False)
        instance.ip_address = get_ip_address(self.request)
        instance.save()
        EmailMessage(
            from_email="support@Aera.com",
            subject="Aera",
            to=["support@Aera.com"],
            body=f"{name}\n{email}\n{message}",
        ).send(fail_silently=True)
        return super().form_valid(form)


class SubScribeView(TemplateView):
    model = Subscribe
    form_class = SubscribeForm
    template_name = "posts/posts.html"

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        obj, created = Subscribe.objects.get_or_create(email=data["email"])
        obj.name = data["name"]
        obj.ip_address = get_ip_address(self.request)
        obj.save()
        if created:
            subscriber_email = EmailMessage(
                subject="Aera",
                body=f"Subscribed to our Aera Newsettler",
                from_email="admin@Aera.com",
                to=[f'{data["email"]}'],
            )
            subscriber_email.send(fail_silently=True)
            support_email = EmailMessage(
                subject="Aera",
                body=f'{data["name"]}\n{data["email"]}\n Subscribed to our Aera Newsettler',
                from_email="admin@Aera.com",
                to=["support@Aera.com"],
            )
            support_email.send(fail_silently=True)
        return JsonResponse({"data": data, "created": created}, safe=False)


class PrivacyPolicyView(TemplateView):
    template_name = "posts/privacy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RobotstxtView(TemplateView):
    template_name = "posts/robots.txt"
    content_type = "text/plain"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AdstxtView(TemplateView):
    template_name = "posts/ads.txt"
    content_type = "text/plain"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def error_404_view(request, exception):
    return render(request, "404.html")


def error_500_view(request):
    return render(request, "500.html")


def error_403_view(request, exception):
    return render(request, "403.html")


def error_400_view(request, exception):
    return render(request, "400.html")
