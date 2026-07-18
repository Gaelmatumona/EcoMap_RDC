from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.liste_affectations,
        name="liste_affectations"
    ),

    path(
        "nouveau/<int:signalement_id>/",
        views.creer_affectation,
        name="creer_affectation"
    ),

    path(
        "rapports/",
        views.liste_rapports,
        name="liste_rapports"
    ),

    path(
        "<int:pk>/",
        views.detail_affectation,
        name="detail_affectation"
    ),

    path(
        "<int:pk>/demarrer/",
        views.demarrer_affectation,
        name="demarrer_affectation"
    ),

    path(
        "<int:pk>/terminer/",
        views.terminer_affectation,
        name="terminer_affectation"
    ),

    path(
        "<int:pk>/rapport/",
        views.creer_rapport,
        name="creer_rapport"
    ),

]