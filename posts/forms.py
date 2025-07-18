from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from django.core.validators import ValidationError
from django.core import validators
from django.contrib.auth.password_validation import validate_password

from posts.models import Contact, Subscribe, PostComments


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message',]

class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscribe
        fields = ['email',]

class PostCommentsForm(forms.ModelForm):

    class Meta:
        model = PostComments
        fields = ['comment']
