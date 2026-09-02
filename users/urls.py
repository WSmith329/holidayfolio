from django.urls import path

from .views import UserCreateView

# Ensure there's no clashes with django.contrib.auth.urls
urlpatterns = [
    path('sign-up/', UserCreateView.as_view(), name='user-create'),
]