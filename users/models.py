from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Utilisateur(AbstractUser):
    """L'abstract User est une héritance du modèlde de base User fournit par django.contrib.auth.User
    Il nous permet d'ajouter des champs, et de définir également leur priorité (par exemple, utiliser l'email comme moyen d'authentification
    """
    phone_number = models.CharField(max_length=60, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    requests_admin_right = models.BooleanField(default=False)

    #is_admin = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username