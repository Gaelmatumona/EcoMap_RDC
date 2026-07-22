from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from .models import (
    Signalement,
    CategorieSignalement,
    PhotoSignalement,
)
from .forms import SignalementForm


@login_required
def liste_signalements(request):

    if request.user.is_staff:

        signalements = Signalement.objects.select_related(
            "categorie",
            "utilisateur",
            "lieu"
        ).order_by("-date_signalement")

    else:

        signalements = Signalement.objects.select_related(
            "categorie",
            "utilisateur",
            "lieu"
        ).filter(
            utilisateur=request.user
        ).order_by("-date_signalement")

    categorie = request.GET.get("categorie")
    statut = request.GET.get("statut")
    recherche = request.GET.get("q")

    if categorie:
        signalements = signalements.filter(
            categorie_id=categorie
        )

    if statut:
        signalements = signalements.filter(
            statut=statut
        )

    if recherche:
        signalements = signalements.filter(
            titre__icontains=recherche
        )

    categories = CategorieSignalement.objects.all()

    return render(
        request,
        "signalements/liste.html",
        {
            "signalements": signalements,
            "categories": categories,
            "statut_choices": Signalement.Statut.choices,
        }
    )


@login_required
def ajouter_signalement(request):

    if request.method == "POST":

        form = SignalementForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            signalement = form.save(commit=False)

            signalement.utilisateur = request.user

            signalement.latitude = request.session.get("latitude")

            signalement.longitude = request.session.get("longitude")

            signalement.statut = Signalement.Statut.EN_ATTENTE

            signalement.save()

            form.save_m2m()

            # Enregistrer toutes les photos
            for photo in request.FILES.getlist("photos"):

                PhotoSignalement.objects.create(
                    signalement=signalement,
                    photo=photo
                )

            messages.success(
                request,
                "Votre signalement a été envoyé avec succès."
            )

            return redirect("liste_signalements")

    else:

        form = SignalementForm()

    return render(
        request,
        "signalements/form.html",
        {
            "form": form,
            "titre": "Nouveau signalement",
        }
    )


@login_required
def detail_signalement(request, pk):

    if request.user.is_staff:

        signalement = get_object_or_404(
            Signalement,
            pk=pk
        )

    else:

        signalement = get_object_or_404(
            Signalement,
            pk=pk,
            utilisateur=request.user
        )

    return render(
        request,
        "signalements/detail.html",
        {
            "signalement": signalement
        }
    )


@login_required
def export_pdf(request):

    response = HttpResponse(
        content_type="application/pdf"
    )

    response["Content-Disposition"] = (
        'attachment; filename="signalements.pdf"'
    )

    document = SimpleDocTemplate(response)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Liste des signalements EcoMap RDC",
            styles["Heading1"]
        )
    )

    data = [[
        "Titre",
        "Catégorie",
        "Statut",
        "Date"
    ]]

    if request.user.is_staff:

        signalements = Signalement.objects.select_related(
            "categorie"
        ).order_by("-date_signalement")

    else:

        signalements = Signalement.objects.select_related(
            "categorie"
        ).filter(
            utilisateur=request.user
        ).order_by("-date_signalement")

    for s in signalements:

        data.append([
            s.titre,
            s.categorie.nom,
            s.get_statut_display(),
            s.date_signalement.strftime("%d/%m/%Y")
        ])

    table = Table(data)

    table.setStyle(

        TableStyle([

            ("BACKGROUND", (0, 0), (-1, 0), colors.darkgreen),

            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

            ("GRID", (0, 0), (-1, -1), 1, colors.black),

            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),

            ("ALIGN", (0, 0), (-1, -1), "CENTER"),

            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),

        ])

    )

    elements.append(table)

    document.build(elements)

    return response