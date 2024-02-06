from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.template import loader
from rest_framework.response import Response
from django.db.models import Sum
from datagold.models import Client, Collecte
from datagold.serializers import CollecteSerializer, ClientSerializer
import pandas as pd
import requests



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


from django.http import JsonResponse, request
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



def Accueil(request):
    # Faire une requête GET vers votre API
    api_url = "http://localhost:8000/api/sociopro/"  # Remplacez cela par l'URL réelle de votre API
    response = requests.get(api_url)


    # Vérifier si la requête a réussi (code 200 OK)
    if response.status_code == 200:
        # Récupérer les données JSON de la réponse
        api_data = response.json()

        # Extraire les labels et les données du JSON
        labels = [entry['categorie_socioprofessionnelle'] for entry in api_data]
        data = [entry['prix_panier_client'] for entry in api_data]

        # Reste du code pour le rendu dans votre template
        return render(request, "index.html", {'labels': labels, 'data': data})
    else:
        # Gérer les erreurs de requête si nécessaire
        return HttpResponse(f"Erreur de requête vers l'API: {response.status_code}", status=response.status_code)

def Moyenne(request):
    api_url = "http://localhost:8000/api/sociopromoyenne/"  # Remplacez cela par l'URL réelle de votre API
    response = requests.get(api_url)
        # Vérifier si la requête a réussi (code 200 OK)
    if response.status_code == 200:
        # Récupérer les données JSON de la réponse
        api_data = response.json()

        # Extraire les labels et les données du JSON
        labels = [entry['categorie_socioprofessionnelle'] for entry in api_data]
        data = [entry['prix_panier_client'] for entry in api_data]

        # Renvoyer les données au format JSON
        return JsonResponse({'labels': labels, 'data': data})
    else:
        # Gérer les erreurs de requête si nécessaire
        return JsonResponse({'error': f"Erreur de requête vers l'API: {response.status_code}"}, status=500)


