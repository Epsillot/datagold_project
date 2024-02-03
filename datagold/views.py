

from rest_framework.views import APIView
from rest_framework.response import Response

from datagold.models import Client, Collecte, Categorie, DetailCollecte
from datagold.serializers import ClientSerializer
from datagold.serializers import CollecteSerializer
class ClientAPIView(APIView):

    def get(self, *args, **kwargs):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

class CollecteAPIView(APIView):

    def get(self, *args, **kwargs):
        collecte = Collecte.objects.all()
        serializer = CollecteSerializer(collecte, many=True)
        return Response(serializer.data)
