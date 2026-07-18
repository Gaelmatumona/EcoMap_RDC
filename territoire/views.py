from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Lieu
from .forms import LieuForm


@login_required
def liste_lieux(request):

    recherche = request.GET.get("q")

    lieux = Lieu.objects.select_related(
        "avenue",
        "avenue__quartier",
        "avenue__quartier__commune"
    )

    if recherche:
        lieux = lieux.filter(nom__icontains=recherche)

    return render(
        request,
        "territoire/liste.html",
        {
            "lieux": lieux.order_by("nom")
        }
    )


@login_required
def ajouter_lieu(request):

    if request.method == "POST":

        form = LieuForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Lieu ajouté avec succès."
            )

            return redirect("liste_lieux")

    else:

        form = LieuForm()

    return render(
        request,
        "territoire/form.html",
        {
            "form": form,
            "titre": "Ajouter un lieu"
        }
    )


@login_required
def modifier_lieu(request, pk):

    lieu = get_object_or_404(Lieu, pk=pk)

    if request.method == "POST":

        form = LieuForm(request.POST, instance=lieu)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Lieu modifié avec succès."
            )

            return redirect("liste_lieux")

    else:

        form = LieuForm(instance=lieu)

    return render(
        request,
        "territoire/form.html",
        {
            "form": form,
            "titre": "Modifier un lieu"
        }
    )


@login_required
def supprimer_lieu(request, pk):

    lieu = get_object_or_404(Lieu, pk=pk)

    if request.method == "POST":

        lieu.delete()

        messages.success(
            request,
            "Lieu supprimé avec succès."
        )

        return redirect("liste_lieux")

    return render(
        request,
        "territoire/supprimer.html",
        {
            "lieu": lieu
        }
    )


@login_required
def detail_lieu(request, pk):

    lieu = get_object_or_404(
        Lieu.objects.select_related(
            "avenue",
            "avenue__quartier",
            "avenue__quartier__commune"
        ),
        pk=pk
    )

    return render(
        request,
        "territoire/detail.html",
        {
            "lieu": lieu
        }
    )