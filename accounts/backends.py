from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import Utilisateur


class CustomAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get("username")

        try:
            user = Utilisateur.objects.get(
                Q(username=username) |
                Q(email=username) |
                Q(telephone=username)
            )
        except Utilisateur.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None