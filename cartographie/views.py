from django.shortcuts import render
from django.http import JsonResponse

from territoire.models import Lieu
from signalements.models import Signalement


def carte(request):

    lieux = Lieu.objects.exclude(
        latitude__isnull=True,
        longitude__isnull=True
    )

    signalements = Signalement.objects.exclude(
        latitude__isnull=True,
        longitude__isnull=True
    ).select_related(
        "categorie",
        "utilisateur"
    )

    return render(
        request,
        "cartographie/carte.html",
        {
            "lieux": lieux,
            "signalements": signalements,
        }
    )


def enregistrer_position(request):

    request.session["latitude"] = request.GET.get("latitude")
    request.session["longitude"] = request.GET.get("longitude")

    return JsonResponse(
        {
            "success": True
        }
    )