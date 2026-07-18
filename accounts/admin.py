from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Utilisateur, Role
from .forms import UtilisateurCreationForm


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("nom",)
    search_fields = ("nom",)


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):

    add_form = UtilisateurCreationForm

    model = Utilisateur

    list_display = (
        "username",
        "nom",
        "postnom",
        "prenom",
        "telephone",
        "email",
        "role",
        "is_staff",
    )

    search_fields = (
        "username",
        "nom",
        "postnom",
        "prenom",
        "telephone",
        "email",
    )

    ordering = ("username",)

    fieldsets = (
        ("Informations", {
            "fields": (
                "username",
                "password",
                "nom",
                "postnom",
                "prenom",
                "telephone",
                "email",
                "sexe",
                "photo",
                "role",
            )
        }),

        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),

        ("Dates", {
            "fields": (
                "last_login",
                "date_joined",
            )
        }),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "nom",
                    "postnom",
                    "prenom",
                    "telephone",
                    "email",
                    "sexe",
                    "role",
                    "password1",
                    "password2",
                ),
            },
        ),
    )