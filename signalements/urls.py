from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.liste_signalements,
        name="liste_signalements"
    ),

    path(
        "ajouter/",
        views.ajouter_signalement,
        name="ajouter_signalement"
    ),

    path(
        "<int:pk>/",
        views.detail_signalement,
        name="detail_signalement"
    ),

    path(
        "export/pdf/",
        views.export_pdf,
        name="export_pdf"
    ),

]