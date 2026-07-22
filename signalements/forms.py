from django import forms
from .models import Signalement


class SignalementForm(forms.ModelForm):

    class Meta:
        model = Signalement

        fields = [
            "categorie",
            "lieu",
            "titre",
            "description",
            "latitude",
            "longitude",
        ]

        widgets = {

            "titre": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "categorie": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "lieu": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5
                }
            ),

            "latitude": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "readonly": "readonly"
                }
            ),

            "longitude": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "readonly": "readonly"
                }
            ),

        }