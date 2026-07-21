from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UtilisateurCreationForm, LoginForm
from signalements.models import Signalement


def inscription(request):

    if request.user.is_authenticated:
        return redirect("profil")

    if request.method == "POST":

        form = UtilisateurCreationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter."
            )

            return redirect("login")

    else:

        form = UtilisateurCreationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


def connexion(request):

    if request.user.is_authenticated:
        return redirect("profil")

    form = LoginForm(request.POST or None)

    if request.method == "POST":

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                messages.success(
                    request,
                    f"Bienvenue {user.prenom}."
                )

                return redirect("profil")

            else:

                messages.error(
                    request,
                    "Nom d'utilisateur ou mot de passe incorrect."
                )

    return render(
        request,
        "accounts/login.html",
        {
            "form": form
        }
    )


@login_required
def profil(request):

    mes_signalements = Signalement.objects.filter(
        utilisateur=request.user
    )

    total = mes_signalements.count()

    en_attente = mes_signalements.filter(
        statut=Signalement.Statut.EN_ATTENTE
    ).count()

    en_cours = mes_signalements.filter(
        statut=Signalement.Statut.EN_COURS
    ).count()

    resolus = mes_signalements.filter(
        statut=Signalement.Statut.RESOLU
    ).count()

    return render(
        request,
        "accounts/profile.html",
        {
            "total": total,
            "en_attente": en_attente,
            "en_cours": en_cours,
            "resolus": resolus,
        }
    )


@login_required
def deconnexion(request):

    logout(request)

    messages.success(
        request,
        "Vous êtes maintenant déconnecté."
    )

    return redirect("login")