from django.shortcuts import render
from django.db.models import Count

from signalements.models import Signalement, CategorieSignalement
from interventions.models import Affectation
from territoire.models import Commune


def dashboard(request):

    total_signalements = Signalement.objects.count()

    en_attente = Signalement.objects.filter(
        statut=Signalement.Statut.EN_ATTENTE
    ).count()

    en_cours = Signalement.objects.filter(
        statut=Signalement.Statut.EN_COURS
    ).count()

    resolus = Signalement.objects.filter(
        statut=Signalement.Statut.RESOLU
    ).count()

    rejetes = Signalement.objects.filter(
        statut=Signalement.Statut.REJETE
    ).count()

    total_affectations = Affectation.objects.count()

    categories = CategorieSignalement.objects.annotate(
        total=Count("signalements")
    ).order_by("-total")

    communes = Commune.objects.annotate(
        total=Count(
            "quartiers__avenues__lieux__signalements"
        )
    ).order_by("-total")

    derniers_signalements = Signalement.objects.select_related(
        "categorie",
        "utilisateur",
        "lieu"
    ).order_by("-date_signalement")[:10]

    return render(
        request,
        "dashboard/index.html",
        {
            "total_signalements": total_signalements,
            "en_attente": en_attente,
            "en_cours": en_cours,
            "resolus": resolus,
            "rejetes": rejetes,
            "total_affectations": total_affectations,
            "categories": categories,
            "communes": communes,
            "derniers_signalements": derniers_signalements,
        }
    )