from django.db import models
from django.conf import settings
from territoire.models import Lieu


class CategorieSignalement(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Catégorie de signalement"
        verbose_name_plural = "Catégories de signalement"
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class Signalement(models.Model):

    class Statut(models.TextChoices):
        EN_ATTENTE = "EN_ATTENTE", "En attente"
        EN_COURS = "EN_COURS", "En cours"
        RESOLU = "RESOLU", "Résolu"
        REJETE = "REJETE", "Rejeté"

    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="signalements"
    )

    categorie = models.ForeignKey(
        CategorieSignalement,
        on_delete=models.PROTECT,
        related_name="signalements"
    )

    lieu = models.ForeignKey(
        Lieu,
        on_delete=models.PROTECT,
        related_name="signalements"
    )

    titre = models.CharField(max_length=200)

    description = models.TextField()

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

    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.EN_ATTENTE
    )

    date_signalement = models.DateTimeField(auto_now_add=True)

    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Signalement"
        verbose_name_plural = "Signalements"
        ordering = ["-date_signalement"]

    def __str__(self):
        return self.titre


class PhotoSignalement(models.Model):

    signalement = models.ForeignKey(
        Signalement,
        on_delete=models.CASCADE,
        related_name="photos"
    )

    photo = models.ImageField(
        upload_to="signalements/"
    )

    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Photo de signalement"
        verbose_name_plural = "Photos des signalements"

    def __str__(self):
        return f"Photo {self.id} - {self.signalement.titre}"