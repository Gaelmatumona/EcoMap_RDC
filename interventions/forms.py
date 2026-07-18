from django import forms

from .models import (
    Affectation,
    RapportIntervention
)


class AffectationForm(forms.ModelForm):

    class Meta:

        model = Affectation

        fields = [

            "service",
            "responsable",
            "date_debut",
            "date_fin",
            "statut",
            "commentaire",

        ]

        widgets = {

            "service": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "responsable": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "date_debut": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),

            "date_fin": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),

            "statut": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "commentaire": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),

        }


class RapportInterventionForm(forms.ModelForm):

    class Meta:

        model = RapportIntervention

        fields = [

            "description",
            "photo_avant",
            "photo_apres",

        ]

        widgets = {

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Décrivez l'intervention réalisée...",
                }
            ),

            "photo_avant": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "photo_apres": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

        }