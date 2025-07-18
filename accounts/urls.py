from django.urls import path
from accounts.views import ProfileView, SettingsUpdateView, ProfileUpdateView, SignUpView, LogInView, LogOutView

app_name = 'auth'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/<slug:slug>/', ProfileView.as_view(), name='profile'),
    path('profile/<slug:slug>/update/', ProfileUpdateView.as_view(), name='profileupdate'),
    path('settings/<int:pk>/', SettingsUpdateView.as_view(), name='settings'),

]
