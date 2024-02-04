from django.db import models

# Create your models here.

from django.db import models


class Collecte(models.Model):
    collecte = models.IntegerField()
    categorie_article = models.CharField(max_length=255)
    prix_article = models.DecimalField(max_digits=10, decimal_places=2)


class Client(models.Model):
    client_anonym = models.CharField(null=True, max_length=255)
    nombre_enfants = models.IntegerField(null=True)
    categorie_socioprofessionnelle = models.CharField(max_length=255)
    prix_panier_client = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    collecte_achat = models.IntegerField(null=True)
