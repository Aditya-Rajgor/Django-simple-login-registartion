from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    # Add more paths here
    path("signup/", views.authView, name="signup"),
]
