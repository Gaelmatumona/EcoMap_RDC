from django.core.management.base import BaseCommand

from territoire.models import Commune, Quartier


class Command(BaseCommand):

    help = "Ajoute les quartiers de Kinshasa"

    def handle(self, *args, **kwargs):

        donnees = {

            "Limete": [
                "Résidentiel",
                "Industriel",
                "Mombele",
                "Kingabwa",
                "Mososo"
            ],

            "Lemba": [
                "Salongo",
                "Livulu",
                "Gombele",
                "Molo"
            ],

            "Matete": [
                "Debonhomme",
                "Totaka",
                "Maziba"
            ],

            "Masina": [
                "Petro Congo",
                "Sans Fil",
                "Mapela",
                "Abattoir"
            ],

            "Ngaliema": [
                "Binza Météo",
                "Binza Ozone",
                "Joli Parc",
                "UPN"
            ],

            "Gombe": [
                "Commerce",
                "Administratif",
                "Résidentiel"
            ]

        }

        for nom_commune, quartiers in donnees.items():

            commune = Commune.objects.get(nom=nom_commune)

            for quartier in quartiers:

                Quartier.objects.get_or_create(
                    nom=quartier,
                    commune=commune
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Quartiers ajoutés avec succès."
            )
        )