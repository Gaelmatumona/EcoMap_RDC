from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from signalements.models import Signalement
from .models import Affectation, RapportIntervention
from .forms import AffectationForm, RapportInterventionForm

from notifications.models import Notification


@login_required
def liste_affectations(request):

    if not request.user.is_staff:
        messages.error(request, "Accès réservé à l'administrateur.")
        return redirect("accueil")

    affectations = Affectation.objects.select_related(
        "signalement",
        "service",
        "responsable"
    ).order_by("-date_affectation")

    return render(
        request,
        "interventions/liste.html",
        {
            "affectations": affectations
        }
    )


@login_required
def detail_affectation(request, pk):

    if not request.user.is_staff:
        messages.error(request, "Accès réservé à l'administrateur.")
        return redirect("accueil")

    affectation = get_object_or_404(
        Affectation.objects.select_related(
            "signalement",
            "service",
            "responsable"
        ),
        pk=pk
    )

    return render(
        request,
        "interventions/detail.html",
        {
            "affectation": affectation
        }
    )


@login_required
def creer_affectation(request, signalement_id):

    if not request.user.is_staff:
        messages.error(request, "Accès réservé à l'administrateur.")
        return redirect("liste_signalements")

    signalement = get_object_or_404(
        Signalement,
        pk=signalement_id
    )

    if request.method == "POST":

        form = AffectationForm(request.POST)

        if form.is_valid():

            affectation = form.save(commit=False)
            affectation.signalement = signalement
            affectation.save()

            Notification.objects.create(
                utilisateur=signalement.utilisateur,
                titre="Signalement affecté",
                message=f"Votre signalement '{signalement.titre}' a été affecté au service {affectation.service.nom}."
            )

            signalement.statut = Signalement.Statut.EN_COURS
            signalement.save()

            messages.success(
                request,
                "Affectation créée avec succès."
            )

            return redirect("liste_affectations")

    else:

        form = AffectationForm()

    return render(
        request,
        "interventions/creer.html",
        {
            "form": form,
            "signalement": signalement,
        }
    )


@login_required
def demarrer_affectation(request, pk):

    if not request.user.is_staff:
        messages.error(request, "Accès réservé à l'administrateur.")
        return redirect("accueil")

    affectation = get_object_or_404(
        Affectation,
        pk=pk
    )

    affectation.statut = Affectation.Statut.EN_COURS
    affectation.date_debut = timezone.now()
    affectation.save()

    Notification.objects.create(
        utilisateur=affectation.signalement.utilisateur,
        titre="Intervention démarrée",
        message=f"L'intervention concernant '{affectation.signalement.titre}' vient de commencer."
    )

    messages.success(
        request,
        "Intervention démarrée."
    )

    return redirect(
        "detail_affectation",
        pk=pk
    )


@login_required
def terminer_affectation(request, pk):

    if not request.user.is_staff:
        messages.error(request, "Accès réservé à l'administrateur.")
        return redirect("accueil")

    affectation = get_object_or_404(
        Affectation,
        pk=pk
    )

    affectation.statut = Affectation.Statut.TERMINEE
    affectation.date_fin = timezone.now()
    affectation.save()

    signalement = affectation.signalement
    signalement.statut = Signalement.Statut.RESOLU
    signalement.save()

    Notification.objects.create(
        utilisateur=signalement.utilisateur,
        titre="Intervention terminée",
        message=f"Votre signalement '{signalement.titre}' a été résolu."
    )

    messages.success(
        request,
        "Intervention terminée."
    )

    return redirect(
        "detail_affectation",
        pk=pk
    )


@login_required
def creer_rapport(request, pk):

    if not request.user.is_staff:
        messages.error(request, "Accès réservé à l'administrateur.")
        return redirect("accueil")

    affectation = get_object_or_404(
        Affectation,
        pk=pk
    )

    if hasattr(affectation, "rapport"):

        messages.warning(
            request,
            "Ce rapport existe déjà."
        )

        return redirect(
            "detail_affectation",
            pk=pk
        )

    if request.method == "POST":

        form = RapportInterventionForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            rapport = form.save(commit=False)
            rapport.affectation = affectation
            rapport.save()

            messages.success(
                request,
                "Rapport enregistré avec succès."
            )

            return redirect(
                "detail_affectation",
                pk=pk
            )

    else:

        form = RapportInterventionForm()

    return render(
        request,
        "interventions/rapport.html",
        {
            "form": form,
            "affectation": affectation,
        }
    )


@login_required
def liste_rapports(request):

    if not request.user.is_staff:
        messages.error(request, "Accès réservé à l'administrateur.")
        return redirect("accueil")

    rapports = RapportIntervention.objects.select_related(
        "affectation",
        "affectation__signalement"
    ).order_by("-date_creation")

    return render(
        request,
        "interventions/liste_rapports.html",
        {
            "rapports": rapports
        }
    )