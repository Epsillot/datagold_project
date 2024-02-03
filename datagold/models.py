from django.db import models

# Create your models here.

from django.db import models

class Client(models.Model):
    nombre_enfants = models.IntegerField()
    categorie_socioprofessionnelle = models.CharField(max_length=255)
    prix_panier_client = models.DecimalField(max_digits=10, decimal_places=2)

class Collecte(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    prix_panier_total = models.DecimalField(max_digits=10, decimal_places=2)

class Categorie(models.Model):
    libelle_categorie = models.CharField(max_length=255)

class DetailCollecte(models.Model):
    collecte = models.ForeignKey(Collecte, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    montant_depense = models.DecimalField(max_digits=10, decimal_places=2)
