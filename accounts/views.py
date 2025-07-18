from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


from accounts.models import User, Profile
from accounts.forms import UserCreationForm, UserUpdateForm, ProfileForm

# Create your views here.

class SignUpView(CreateView):
    template_name = 'auth/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('auth:login')

class LogInView(LoginView):
    template_name = 'auth/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('posts:posts')
    redirect_authenticated_user = True
    
class LogOutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('posts:posts')

class SettingsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    login_url = reverse_lazy('auth:login')
    template_name = 'auth/settings.html'
    form_class = UserUpdateForm

    def get_login_url(self):
        return self.login_url
    
    def test_func(self):
        self.object = self.get_object()
        return self.request.user.is_authenticated and self.request.user.is_superuser or self.request.user.is_staff or self.object == self.request.user

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('auth:settings', kwargs={'pk': self.get_object().pk})
    
class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    login_url = reverse_lazy('auth:login')
    template_name = 'auth/profile.html'
    form_class = ProfileForm
    
    def get_success_url(self):
        return reverse_lazy('auth:profile', kwargs={'slug': self.get_object().slug})
    
class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    login_url = reverse_lazy('auth:login')
    template_name = 'auth/profileupdate.html'
    form_class = ProfileForm

    def get_login_url(self):
        return self.login_url
    
    def test_func(self):
        self.object = self.get_object()
        return self.request.user.is_authenticated and self.request.user.is_superuser or self.request.user.is_staff or self.object == self.request.user

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('auth:profileupdate', kwargs={'slug': self.get_object().slug})

