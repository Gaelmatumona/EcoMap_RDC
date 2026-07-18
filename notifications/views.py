from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Notification


@login_required
def liste_notifications(request):

    notifications = Notification.objects.filter(

        utilisateur=request.user

    )

    return render(

        request,

        "notifications/liste.html",

        {

            "notifications": notifications

        }

    )