from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from posts.models import Contact, Post, Subscribe, PostComments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "seo_title",
            "seo_description",
            "slug",
            "category",
            "status",
            "image",
            "description",
        ]
        widgets = {
            "description": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ["email"]


class PostCommentsForm(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ["comment"]
