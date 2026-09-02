from django.urls import path

from .views import UserCreateView, ProfileDetailView

# Ensure there's no clashes with django.contrib.auth.urls
urlpatterns = [
    path('sign-up/', UserCreateView.as_view(), name='user-create'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
]