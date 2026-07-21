from django.urls import path
from . import views

urlpatterns = [

    path(
        "inscription/",
        views.inscription,
        name="register"
    ),

    path(
        "connexion/",
        views.connexion,
        name="login"
    ),

    path(
        "profil/",
        views.profil,
        name="profil"
    ),

    path(
        "deconnexion/",
        views.deconnexion,
        name="logout"
    ),

]