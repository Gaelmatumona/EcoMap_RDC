from django.contrib import admin
from .models import (
    Service,
    Affectation,
    RapportIntervention
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nom",
        "telephone",
        "email",
    )

    search_fields = (
        "nom",
    )


@admin.register(Affectation)
class AffectationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "signalement",
        "service",
        "responsable",
        "statut",
        "date_affectation",
    )

    list_filter = (
        "statut",
        "service",
    )

    search_fields = (
        "signalement__titre",
        "service__nom",
    )


@admin.register(RapportIntervention)
class RapportInterventionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "affectation",
        "date_creation",
    )

    search_fields = (
        "affectation__signalement__titre",
    )