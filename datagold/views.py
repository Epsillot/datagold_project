from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models import Avg
from datagold.models import Client, Collecte
from datagold.serializers import CollecteSerializer, ClientSerializer


class ClientAPIView(APIView):
    def get(self, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

class CollecteAPIView(APIView):
    def get(self, *args, **kwargs):
        collectes = Collecte.objects.all()
        serializer = CollecteSerializer(collectes, many=True)
        return Response(serializer.data)

class PanierSocioProAPIView(APIView):
    def get(self, *args, **kwargs):
        # Requête pour obtenir la somme de "prix_panier_client" par "categorie_socioprofessionnelle"
        result = (
            Client.objects.values('categorie_socioprofessionnelle' , 'date')
            .annotate(somme_prix_panier_total=Sum('prix_panier_client'))
            .order_by('categorie_socioprofessionnelle', 'date')
        )
        return Response(result)


class DepenseMoyennePanierAPIView(APIView):
    def get(self, *args, **kwargs):
        # Requête pour obtenir la dépense moyenne du panier par "categorie_socioprofessionnelle"
        result = (
            Client.objects.values('categorie_socioprofessionnelle', 'date')
            .annotate(depense_moyenne_panier=Avg('prix_panier_client'))
            .order_by('categorie_socioprofessionnelle', 'date')
        )
        return Response(result)