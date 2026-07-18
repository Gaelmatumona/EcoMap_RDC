from django.contrib import admin
from .models import Province, Ville, Commune, Quartier, Avenue, Lieu


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ("id", "nom")
    search_fields = ("nom",)


@admin.register(Ville)
class VilleAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "province")
    list_filter = ("province",)
    search_fields = ("nom",)


@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "ville")
    list_filter = ("ville",)
    search_fields = ("nom",)


@admin.register(Quartier)
class QuartierAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "commune")
    list_filter = ("commune",)
    search_fields = ("nom",)


@admin.register(Avenue)
class AvenueAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "quartier")
    list_filter = ("quartier",)
    search_fields = ("nom",)


@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nom",
        "type_lieu",
        "avenue",
        "latitude",
        "longitude",
    )

    list_filter = (
        "type_lieu",
        "avenue",
    )

    search_fields = (
        "nom",
        "description",
    )