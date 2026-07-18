from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UtilisateurCreationForm, LoginForm


def inscription(request):
    if request.method == "POST":
        form = UtilisateurCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé avec succès.")
            return redirect("login")
    else:
        form = UtilisateurCreationForm()

    return render(request, "accounts/register.html", {"form": form})


def connexion(request):
    if request.user.is_authenticated:
        return redirect("profil")

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            identifiant = form.cleaned_data["identifiant"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=identifiant,
                password=password
            )

            if user is not None:
                login(request, user)
                messages.success(request, "Connexion réussie.")
                return redirect("profil")
            else:
                messages.error(
                    request,
                    "Identifiant ou mot de passe incorrect."
                )

    return render(request, "accounts/login.html", {"form": form})


@login_required
def profil(request):
    return render(request, "accounts/profile.html")


@login_required
def deconnexion(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecté.")
    return redirect("login")