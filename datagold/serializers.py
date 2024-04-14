from rest_framework import serializers
from datagold.models import Client, Collecte

class ClientSerializer(serializers.Serializer):
    """
    Serializer pour le modèle Client.

    Ce serializer est utilisé pour convertir les objets Client en JSON
    et vice versa pour les opérations de lecture et d'écriture.

    Attributes:
        categorie_socioprofessionnelle (CharField): Champ de sérialisation pour la catégorie socio-professionnelle du client.
        date (DateField): Champ de sérialisation pour la date de la transaction du client.
        prix_panier_client (FloatField): Champ de sérialisation pour le prix du panier du client.
    """
    categorie_socioprofessionnelle = serializers.CharField()
    date = serializers.DateField()
    prix_panier_client = serializers.FloatField()

class CollecteSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Collecte.

    Ce serializer est utilisé pour convertir les objets Collecte en JSON
    et vice versa pour les opérations de lecture et d'écriture.

    Attributes:
        model (Collecte): Le modèle de données Collecte à sérialiser.
        fields (list): Liste des champs du modèle Collecte à sérialiser.
    """
    class Meta:
        model = Collecte
        fields = '__all__'
