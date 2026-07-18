from django import forms
from .models import Lieu


class LieuForm(forms.ModelForm):

    class Meta:
        model = Lieu

        fields = [
            "avenue",
            "nom",
            "type_lieu",
            "description",
            "latitude",
            "longitude",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }