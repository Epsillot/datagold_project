from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from datagold.models import Client, Collecte
from datagold.serializers import CollecteSerializer, ClientSerializer
import pandas as pd

class ClientAPIView(APIView):
    def get(self, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)

        # Convertir le résultat en JSON
        result_json = serializer.data

        # Afficher le résultat JSON
        return Response(result_json)

class CollecteAPIView(APIView):
    def get(self, *args, **kwargs):
        collectes = Collecte.objects.all()
        serializer = CollecteSerializer(collectes, many=True)

        # Convertir le résultat en JSON
        result_json = serializer.data

        # Afficher le résultat JSON
        return Response(result_json)

from django.http import JsonResponse
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer

class PanierSocioProAPIView(APIView):
    def get(self, *args, **kwargs):
        # Requête pour obtenir les données
        queryset = Client.objects.values('categorie_socioprofessionnelle', 'date', 'prix_panier_client')
        data = list(queryset)

        # Utilise Pandas pour effectuer le calcul
        df = pd.DataFrame(data)
        result = df.groupby(['categorie_socioprofessionnelle', 'date'])['prix_panier_client'].sum().reset_index()

        # Convertir le DataFrame en liste de dictionnaires
        result_array = result.to_dict(orient='records')

        # Convertir le prix_panier_client en format float
        for entry in result_array:
            entry['prix_panier_client'] = float(entry['prix_panier_client'])

        # Utilise le serializer ClientSerializer pour formater la sortie JSON
        serializer = ClientSerializer(result_array, many=True, context={'request': self.request})

        # Afficher le résultat JSON
        return Response(serializer.data)




class DepenseMoyennePanierAPIView(APIView):
    def get(self, *args, **kwargs):
        # Requête pour obtenir les données
        queryset = Client.objects.values('categorie_socioprofessionnelle', 'date', 'prix_panier_client')
        data = list(queryset)

        # Utilise Pandas pour effectuer le calcul
        df = pd.DataFrame(data)

        # Convertir le champ 'prix_panier_client' en type numérique (float)
        df['prix_panier_client'] = pd.to_numeric(df['prix_panier_client'], errors='coerce')

        result = df.groupby(['categorie_socioprofessionnelle', 'date'])['prix_panier_client'].mean().reset_index()

        # Convertir le DataFrame en liste de dictionnaires
        result_array = result.to_dict(orient='records')

        # Convertir le prix_panier_client en format float
        for entry in result_array:
            entry['prix_panier_client'] = float(entry['prix_panier_client'])

        # Utilise le serializer ClientSerializer pour formater la sortie JSON
        serializer = ClientSerializer(result_array, many=True, context={'request': self.request})

        # Afficher le résultat JSON
        return Response(serializer.data)




