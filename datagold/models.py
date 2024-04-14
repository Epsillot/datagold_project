from django.db import models

class Collecte(models.Model):
    """
    Modèle pour la collecte d'articles.

    Ce modèle représente une collecte d'articles avec des informations telles que la quantité collectée,
    la catégorie d'article et le prix de l'article.

    Attributes:
        collecte (IntegerField): La quantité collectée.
        categorie_article (CharField): La catégorie de l'article.
        prix_article (DecimalField): Le prix de l'article.
    """
    collecte = models.IntegerField()
    categorie_article = models.CharField(max_length=255)
    prix_article = models.DecimalField(max_digits=10, decimal_places=2)


class Client(models.Model):
    """
    Modèle pour les clients.

    Ce modèle représente un client avec des informations telles que le client anonyme, le nombre d'enfants,
    la catégorie socio-professionnelle, le prix du panier du client, la date et la collecte d'achat.

    Attributes:
        client_anonym (CharField): Le nom anonyme du client.
        nombre_enfants (IntegerField): Le nombre d'enfants du client.
        categorie_socioprofessionnelle (CharField): La catégorie socio-professionnelle du client.
        prix_panier_client (DecimalField): Le prix du panier du client.
        date (DateField): La date de la transaction.
        collecte_achat (IntegerField): La quantité d'articles achetés lors de la collecte.
    """
    client_anonym = models.CharField(null=True, max_length=255)
    nombre_enfants = models.IntegerField(null=True)
    categorie_socioprofessionnelle = models.CharField(max_length=255)
    prix_panier_client = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    collecte_achat = models.IntegerField(null=True)
