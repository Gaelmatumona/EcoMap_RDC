from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UtilisateurManager


class Role(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "roles"
        verbose_name = "Rôle"
        verbose_name_plural = "Rôles"
        ordering = ["nom"]

    def __str__(self):
        return self.nom


class Utilisateur(AbstractUser):

    class Sexe(models.TextChoices):
        MASCULIN = "M", "Masculin"
        FEMININ = "F", "Féminin"

    # Suppression du username
    username = None

    telephone = models.CharField(
        max_length=15,
        unique=True,
        verbose_name="Numéro de téléphone"
    )

    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    sexe = models.CharField(
        max_length=1,
        choices=Sexe.choices
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    photo = models.ImageField(
        upload_to="utilisateurs/",
        blank=True,
        null=True
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        related_name="utilisateurs"
    )

    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "telephone"
    REQUIRED_FIELDS = ["nom", "postnom", "prenom"]

    objects = UtilisateurManager()

    class Meta:
        db_table = "utilisateurs"
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
        ordering = ["nom", "postnom"]

    def __str__(self):
        return f"{self.nom} {self.postnom} {self.prenom}"