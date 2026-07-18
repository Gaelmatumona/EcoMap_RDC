from django.core.management.base import BaseCommand

from territoire.models import Avenue, Lieu


class Command(BaseCommand):

    help = "Ajoute les principaux lieux de Kinshasa"

    def handle(self, *args, **kwargs):

        donnees = {

            "Boulevard du 30 Juin": [

                ("Gare Centrale", -4.3215, 15.3125),
                ("Hôtel de Ville", -4.3224, 15.3136),
                ("Palais de la Nation", -4.3168, 15.3072),

            ],

            "Avenue By-Pass": [

                ("Université de Kinshasa", -4.4415, 15.2810),
                ("Rond-point Ngaba", -4.4228, 15.3005),

            ],

            "Boulevard Lumumba": [

                ("Aéroport de Ndjili", -4.3858, 15.4446),
                ("Marché de la Liberté", -4.3865, 15.3810),

            ],

            "Avenue Université": [

                ("Université Protestante au Congo", -4.4268, 15.3090),

            ],

            "Avenue Industrielle": [

                ("Zone Industrielle", -4.3388, 15.3382),

            ],

            "Avenue des Aviateurs": [

                ("Immeuble Sozacom", -4.3190, 15.3079),

            ],

        }

        for nom_avenue, lieux in donnees.items():

            try:

                avenue = Avenue.objects.get(nom=nom_avenue)

            except Avenue.DoesNotExist:

                self.stdout.write(
                    self.style.WARNING(
                        f"Avenue introuvable : {nom_avenue}"
                    )
                )

                continue

            for nom, latitude, longitude in lieux:

                Lieu.objects.get_or_create(

                    nom=nom,

                    avenue=avenue,

                    defaults={
                        "latitude": latitude,
                        "longitude": longitude
                    }

                )

        self.stdout.write(
            self.style.SUCCESS(
                "Lieux ajoutés avec succès."
            )
        )