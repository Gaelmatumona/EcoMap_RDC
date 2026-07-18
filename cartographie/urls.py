from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.carte,
        name="carte"
    ),

    path(
        "enregistrer-position/",
        views.enregistrer_position,
        name="enregistrer_position"
    ),

]