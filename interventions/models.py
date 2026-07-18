from django.db import models
from django.conf import settings
from signalements.models import Signalement


class Service(models.Model):
    nom = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nom


class Affectation(models.Model):

    class Statut(models.TextChoices):
        EN_ATTENTE = "EN_ATTENTE", "En attente"
        ASSIGNEE = "ASSIGNEE", "Assignée"
        EN_COURS = "EN_COURS", "En cours"
        TERMINEE = "TERMINEE", "Terminée"
        ANNULEE = "ANNULEE", "Annulée"

    signalement = models.OneToOneField(
        Signalement,
        on_delete=models.CASCADE,
        related_name="affectation"
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="affectations"
    )

    responsable = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    date_affectation = models.DateTimeField(auto_now_add=True)

    date_debut = models.DateTimeField(
        null=True,
        blank=True
    )

    date_fin = models.DateTimeField(
        null=True,
        blank=True
    )

    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.EN_ATTENTE
    )

    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"{self.signalement.titre} - {self.service.nom}"


class RapportIntervention(models.Model):

    affectation = models.OneToOneField(
        Affectation,
        on_delete=models.CASCADE,
        related_name="rapport"
    )

    description = models.TextField()

    photo_avant = models.ImageField(
        upload_to="interventions/avant/"
    )

    photo_apres = models.ImageField(
        upload_to="interventions/apres/"
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rapport {self.affectation.signalement.titre}"
