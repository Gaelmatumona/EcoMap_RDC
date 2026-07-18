from django.core.management.base import BaseCommand
from territoire.models import Commune, Quartier, Avenue


class Command(BaseCommand):
    help = "Ajoute les avenues principales de Kinshasa"

    def handle(self, *args, **kwargs):

        donnees = {

            "Limete": {

                "Résidentiel": [
                    "Avenue Lumumba",
                    "Avenue Industrielle",
                    "Avenue Kasa-Vubu",
                    "Avenue Poids Lourds",
                ],

                "Mombele": [
                    "Avenue Mombele",
                    "Avenue Bongolo",
                    "Avenue Bokassa",
                ],

                "Kingabwa": [
                    "Avenue Kingabwa",
                    "Avenue Congo",
                ],

                "Mososo": [
                    "Avenue Mososo",
                ],

            },

            "Lemba": {

                "Salongo": [
                    "Avenue By-Pass",
                    "Avenue Université",
                ],

                "Livulu": [
                    "Avenue Super Lemba",
                    "Avenue Livulu",
                ],

                "Gombele": [
                    "Avenue Gombele",
                ],

                "Molo": [
                    "Avenue Molo",
                ],

            },

            "Matete": {

                "Debonhomme": [
                    "Avenue Debonhomme",
                    "Avenue Huileries",
                ],

                "Totaka": [
                    "Avenue Totaka",
                ],

                "Maziba": [
                    "Avenue Maziba",
                ],

            },

            "Masina": {

                "Petro Congo": [
                    "Boulevard Lumumba",
                ],

                "Sans Fil": [
                    "Route Mokali",
                ],

                "Mapela": [
                    "Avenue Mapela",
                ],

                "Abattoir": [
                    "Avenue Abattoir",
                ],

            },

            "Ngaliema": {

                "Binza Météo": [
                    "Avenue Binza Météo",
                ],

                "Binza Ozone": [
                    "Avenue Binza Ozone",
                ],

                "Joli Parc": [
                    "Avenue Joli Parc",
                ],

                "UPN": [
                    "Avenue UPN",
                ],

            },

            "Gombe": {

                "Commerce": [
                    "Boulevard du 30 Juin",
                    "Avenue des Aviateurs",
                    "Avenue Colonel Ebeya",
                ],

                "Administratif": [
                    "Avenue de la Justice",
                    "Avenue Wagenia",
                ],

                "Résidentiel": [
                    "Avenue du Port",
                ],

            },

        }

        for nom_commune, quartiers in donnees.items():

            try:

                commune = Commune.objects.get(nom=nom_commune)

            except Commune.DoesNotExist:

                self.stdout.write(
                    self.style.WARNING(
                        f"Commune introuvable : {nom_commune}"
                    )
                )
                continue

            for nom_quartier, avenues in quartiers.items():

                try:

                    quartier = Quartier.objects.get(
                        nom=nom_quartier,
                        commune=commune
                    )

                except Quartier.DoesNotExist:

                    self.stdout.write(
                        self.style.WARNING(
                            f"Quartier introuvable : {nom_quartier}"
                        )
                    )
                    continue

                for nom_avenue in avenues:

                    Avenue.objects.get_or_create(
                        nom=nom_avenue,
                        quartier=quartier
                    )

        self.stdout.write(
            self.style.SUCCESS(
                "Toutes les avenues ont été ajoutées avec succès."
            )
        )