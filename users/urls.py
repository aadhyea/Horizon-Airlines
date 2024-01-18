from django.urls import path
from . import views

app_name = "users"

urlpatterns=[
    path("", views.index, name="index"),
    path("Login", views.login_view, name="login"),
    path("Logout", views.logout_view, name="logout"),
    path("Register", views.register, name = "register")
]