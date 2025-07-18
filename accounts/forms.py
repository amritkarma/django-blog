from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField

from accounts.models import User, Profile


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'phone_no', 'password1', 'password2']


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_no',
                  'is_active', 'is_staff', 'is_superuser']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'phone_no']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'bio']
