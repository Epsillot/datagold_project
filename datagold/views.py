import csv
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from datagold.models import Client, Collecte
from datagold.serializers import ClientSerializer

def custom_page_not_found(request, exception):
    """
    Renvoie une page d'erreur 404 personnalisée.

    Args:
        request: L'objet HttpRequest.
        exception: L'exception qui a déclenché l'erreur.

    Returns:
        Un objet HttpResponse avec le contenu de la page d'erreur 404.
    """
    return render(request, '404.html', status=404)

def custom_server_error(request):
    """
    Renvoie une page d'erreur 500 personnalisée.

    Args:
        request: L'objet HttpRequest.

    Returns:
        Un objet HttpResponse avec le contenu de la page d'erreur 500.
    """
    return render(request, '500.html', status=500)

class ClientAPIView(APIView):
    """
    Vue API pour récupérer les clients.

    Cette vue permet de récupérer tous les clients de la base de données
    et de les sérialiser en JSON.

    Attributes:
        permission_classes (list): Les classes de permission requises pour accéder à cette API.
    """
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        """
        Méthode pour la gestion des requêtes GET.

        Returns:
            Un objet Response contenant les données JSON des clients.
        """
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)

        # Convertir le résultat en JSON
        result_json = serializer.data

        # Afficher le résultat JSON
        return Response(result_json)

class CollecteAPIView(APIView):
    """
    Vue API pour exporter les données de collecte au format CSV.

    Cette vue permet de récupérer les données de collecte de la base de données
    et de les exporter au format CSV.

    Attributes:
        permission_classes (list): Les classes de permission requises pour accéder à cette API.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Méthode pour la gestion des requêtes GET.

        Args:
            request: L'objet HttpRequest.

        Returns:
            Un objet HttpResponse avec les données de collecte exportées au format CSV.
        """
        # Récupérer le nombre de lignes à exporter depuis les paramètres GET
        number_of_rows = int(request.GET.get('numberOfRows', 10))

        # Récupérer les données correspondantes de la base de données
        collectes = Collecte.objects.all()[:number_of_rows]

        # Créer un objet HttpResponse avec le type MIME CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="collectes.csv"'

        # Créer un écrivain CSV et écrire les données dans la réponse HTTP
        writer = csv.writer(response)
        writer.writerow(['collecte', 'categorie_article', 'prix_article'])  # Entêtes de colonnes
        for collecte in collectes:
            writer.writerow(
                [collecte.collecte, collecte.categorie_article, collecte.prix_article])  # Données de chaque ligne

        return response

class PanierSocioProAPIView(APIView):
    """
    Vue API pour calculer le prix moyen du panier par catégorie socio-professionnelle.

    Cette vue permet de récupérer les données de transaction des clients,
    de les traiter à l'aide de Pandas et de renvoyer le résultat au format JSON.

    Attributes:
        permission_classes (list): Les classes de permission requises pour accéder à cette API.
    """
    #permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        """
        Méthode pour la gestion des requêtes GET.

        Returns:
            Un objet Response contenant les données JSON du prix moyen du panier par catégorie socio-professionnelle.
        """
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
    """
    Vue API pour calculer la dépense moyenne par panier par catégorie socio-professionnelle.

    Cette vue permet de récupérer les données de transaction des clients,
    de les traiter à l'aide de Pandas et de renvoyer le résultat au format JSON.

    Attributes:
        permission_classes (list): Les classes de permission requises pour accéder à cette API.
    """
    # permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        """
        Méthode pour la gestion des requêtes GET.

        Returns:
            Un objet Response contenant les données JSON de la dépense moyenne par panier par catégorie socio-professionnelle.
        """
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

@login_required
def Accueil(request):
    """
    Vue pour la page d'accueil.

    Cette vue récupère les données JSON de l'API PanierSocioProAPIView
    et les utilise pour générer un graphique pour la page d'accueil.

    Args:
        request: L'objet HttpRequest.

    Returns:
        Un objet HttpResponse avec le contenu de la page d'accueil.
    """
    # Créer un objet Request factice
    fake_request = HttpRequest()
    fake_request.method = 'GET'
    fake_request.user = request.user  # Si vous avez besoin de l'utilisateur authentifié

    # Instancier la vue PanierSocioProAPIView
    view = PanierSocioProAPIView()

    # Assigner l'objet Request factice à la vue
    view.request = fake_request

    # Appeler la méthode get de la vue
    response = view.get(fake_request)

    # Vérifier si la réponse est un objet Response valide
    if response.status_code == 200:
        # Récupérer les données JSON de la réponse
        api_data = response.data

        # Extraire les labels et les données du JSON
        labels = [entry['categorie_socioprofessionnelle'] for entry in api_data]
        data = [entry['prix_panier_client'] for entry in api_data]

        # Reste du code pour le rendu dans votre template
        return render(request, "index.html", {'labels': labels, 'data': data})
    else:
        # Gérer les erreurs de requête si nécessaire
        return HttpResponse(f"Erreur de requête vers l'API: {response.status_code}", status=response.status_code)

@login_required
def Moyenne(request):
    """
    Vue pour la page de la moyenne.

    Cette vue récupère les données JSON de l'API DepenseMoyennePanierAPIView
    et les utilise pour générer un graphique pour la page de la moyenne.

    Args:
        request: L'objet HttpRequest.

    Returns:
        Un objet JsonResponse avec les données JSON de la page de la moyenne.
    """
    # Créer un objet Request factice
    fake_request = HttpRequest()
    fake_request.method = 'GET'
    fake_request.user = request.user  # Si vous avez besoin de l'utilisateur authentifié

    # Instancier la vue DepenseMoyennePanierAPIView
    view = DepenseMoyennePanierAPIView()

    # Assigner l'objet Request factice à la vue
    view.request = fake_request

    # Appeler la méthode get de la vue
    response = view.get(fake_request)

    # Vérifier si la réponse est un objet Response valide
    if response.status_code == 200:
        # Récupérer les données JSON de la réponse
        api_data = response.data

        # Extraire les labels et les données du JSON
        labels = [entry['categorie_socioprofessionnelle'] for entry in api_data]
        data = [entry['prix_panier_client'] for entry in api_data]

        # Renvoyer les données au format JSON
        return JsonResponse({'labels': labels, 'data': data})
    else:
        # Gérer les erreurs de requête si nécessaire
        return JsonResponse({'error': f"Erreur de requête vers l'API: {response.status_code}"}, status=500)


