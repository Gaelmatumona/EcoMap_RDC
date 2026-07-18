from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.inscription, name="register"),
    path("login/", views.connexion, name="login"),
    path("profile/", views.profil, name="profil"),
    path("logout/", views.deconnexion, name="logout"),
]