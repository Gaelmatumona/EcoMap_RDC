from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur


class UtilisateurCreationForm(UserCreationForm):

    class Meta:
        model = Utilisateur

        fields = [
            "nom",
            "postnom",
            "prenom",
            "username",
            "telephone",
            "sexe",
            "password1",
            "password2",
        ]

        widgets = {

            "nom": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Votre nom",
                "autocomplete": "off"
            }),

            "postnom": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Votre postnom",
                "autocomplete": "off"
            }),

            "prenom": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Votre prénom",
                "autocomplete": "off"
            }),

            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nom d'utilisateur",
                "autocomplete": "off"
            }),

            "telephone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex : +243..."
            }),

            "sexe": forms.Select(attrs={
                "class": "form-select"
            }),

        }

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Mot de passe"
        })
    )

    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Confirmer le mot de passe"
        })
    )


class LoginForm(forms.Form):

    username = forms.CharField(
        label="Nom d'utilisateur",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Nom d'utilisateur"
        })
    )

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Mot de passe"
        })
    )