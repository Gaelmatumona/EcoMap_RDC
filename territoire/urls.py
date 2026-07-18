from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.liste_lieux,
        name="liste_lieux"
    ),

    path(
        "ajouter/",
        views.ajouter_lieu,
        name="ajouter_lieu"
    ),

    path(
        "<int:pk>/",
        views.detail_lieu,
        name="detail_lieu"
    ),

    path(
        "<int:pk>/modifier/",
        views.modifier_lieu,
        name="modifier_lieu"
    ),

    path(
        "<int:pk>/supprimer/",
        views.supprimer_lieu,
        name="supprimer_lieu"
    ),

]