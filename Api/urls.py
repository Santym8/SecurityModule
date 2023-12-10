from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name="login-api"),
    path("register-audit", views.register_audit, name="register-audit-api"),
]