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
            "statut",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5
                }
            )
        }