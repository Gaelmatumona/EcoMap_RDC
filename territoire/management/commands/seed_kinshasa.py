from django.core.management.base import BaseCommand

from territoire.models import Province, Ville, Commune


class Command(BaseCommand):

    help = "Ajoute les données de base de Kinshasa"

    def handle(self, *args, **kwargs):

        province, created = Province.objects.get_or_create(
            nom="Kinshasa"
        )

        ville, created = Ville.objects.get_or_create(
            nom="Kinshasa",
            province=province
        )

        communes = [

            "Bandalungwa",
            "Barumbu",
            "Bumbu",
            "Gombe",
            "Kalamu",
            "Kasa-Vubu",
            "Kimbanseke",
            "Kinshasa",
            "Kintambo",
            "Kisenso",
            "Lemba",
            "Limete",
            "Lingwala",
            "Makala",
            "Maluku",
            "Masina",
            "Matete",
            "Mont-Ngafula",
            "Ndjili",
            "Ngaba",
            "Ngaliema",
            "Ngiri-Ngiri",
            "Nsele",
            "Selembao"

        ]

        for commune in communes:

            Commune.objects.get_or_create(

                nom=commune,

                ville=ville

            )

        self.stdout.write(

            self.style.SUCCESS(

                "Kinshasa a été ajoutée avec succès."

            )

        )