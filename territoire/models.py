from django.db import models


class Province(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class Ville(models.Model):
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="villes"
    )

    nom = models.CharField(max_length=100)

    class Meta:
        ordering = ["nom"]
        unique_together = ("province", "nom")

    def __str__(self):
        return self.nom


class Commune(models.Model):
    ville = models.ForeignKey(
        Ville,
        on_delete=models.CASCADE,
        related_name="communes"
    )

    nom = models.CharField(max_length=100)

    class Meta:
        ordering = ["nom"]
        unique_together = ("ville", "nom")

    def __str__(self):
        return self.nom


class Quartier(models.Model):
    commune = models.ForeignKey(
        Commune,
        on_delete=models.CASCADE,
        related_name="quartiers"
    )

    nom = models.CharField(max_length=100)

    class Meta:
        ordering = ["nom"]
        unique_together = ("commune", "nom")

    def __str__(self):
        return self.nom


class Avenue(models.Model):
    quartier = models.ForeignKey(
        Quartier,
        on_delete=models.CASCADE,
        related_name="avenues"
    )

    nom = models.CharField(max_length=150)

    class Meta:
        ordering = ["nom"]
        unique_together = ("quartier", "nom")

    def __str__(self):
        return self.nom


class Lieu(models.Model):

    class TypeLieu(models.TextChoices):
        MARCHE = "MARCHE", "Marché"
        HOPITAL = "HOPITAL", "Hôpital"
        ECOLE = "ECOLE", "École"
        UNIVERSITE = "UNIVERSITE", "Université"
        ROUTE = "ROUTE", "Route principale"
        GARE = "GARE", "Gare"
        ARRET = "ARRET", "Arrêt de bus"
        ROND_POINT = "ROND_POINT", "Rond-point"
        BATIMENT = "BATIMENT", "Bâtiment public"
        POUBELLE = "POUBELLE", "Poubelle publique"
        RECYCLAGE = "RECYCLAGE", "Centre de recyclage"
        AUTRE = "AUTRE", "Autre"

    avenue = models.ForeignKey(
        Avenue,
        on_delete=models.CASCADE,
        related_name="lieux"
    )

    nom = models.CharField(max_length=200)

    type_lieu = models.CharField(
        max_length=20,
        choices=TypeLieu.choices,
        default=TypeLieu.AUTRE
    )

    description = models.TextField(
        blank=True
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ["nom"]

    def __str__(self):
        return self.nom