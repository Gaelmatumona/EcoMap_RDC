from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Utilisateur(AbstractUser):

    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    telephone = models.CharField(
        max_length=20,
        unique=True
    )

    sexe = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Masculin'),
            ('F', 'Féminin'),
        ]
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
        blank=True
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.postnom} {self.prenom}"