from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur


class UtilisateurCreationForm(UserCreationForm):

    class Meta:
        model = Utilisateur
        fields = (
            "username",
            "nom",
            "postnom",
            "prenom",
            "telephone",
            "email",
            "sexe",
            "photo",
            "role",
            "password1",
            "password2",
        )


class LoginForm(forms.Form):
    identifiant = forms.CharField(
        label="Nom d'utilisateur / Email / Téléphone",
        max_length=150
    )

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput
    )