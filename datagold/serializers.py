from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from datagold.models import Client, Collecte

class ClientSerializer(serializers.Serializer):
    categorie_socioprofessionnelle = serializers.CharField()
    date = serializers.DateField()
    prix_panier_client = serializers.FloatField()

class CollecteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collecte
        fields = '__all__'


