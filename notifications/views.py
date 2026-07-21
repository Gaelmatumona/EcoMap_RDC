from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Notification


@login_required
def liste_notifications(request):

    if request.user.is_staff:

        notifications = Notification.objects.all().order_by("-date_creation")

    else:

        notifications = Notification.objects.filter(
            utilisateur=request.user
        ).order_by("-date_creation")

    return render(

        request,

        "notifications/liste.html",

        {

            "notifications": notifications

        }

    )