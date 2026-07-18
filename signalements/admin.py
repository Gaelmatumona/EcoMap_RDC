from django.contrib import admin
from .models import (
    CategorieSignalement,
    Signalement,
    PhotoSignalement
)


@admin.register(CategorieSignalement)
class CategorieSignalementAdmin(admin.ModelAdmin):
    list_display = ("id", "nom")
    search_fields = ("nom",)


class PhotoSignalementInline(admin.TabularInline):
    model = PhotoSignalement
    extra = 1


@admin.register(Signalement)
class SignalementAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "titre",
        "utilisateur",
        "categorie",
        "lieu",
        "statut",
        "date_signalement",
    )

    list_filter = (
        "categorie",
        "statut",
        "date_signalement",
    )

    search_fields = (
        "titre",
        "description",
        "utilisateur__username",
        "utilisateur__nom",
        "utilisateur__postnom",
        "utilisateur__prenom",
    )

    readonly_fields = (
        "date_signalement",
        "date_modification",
    )

    inlines = [PhotoSignalementInline]


@admin.register(PhotoSignalement)
class PhotoSignalementAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "signalement",
        "date_ajout",
    )

    search_fields = (
        "signalement__titre",
    )
