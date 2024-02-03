from rest_framework.serializers import ModelSerializer

from datagold.models import Client, Collecte, Categorie, DetailCollecte

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CollecteSerializer:
    class Meta:
        model = Collecte
        fields = '__all__'


class CategorieSerializer:
    class Meta:
        model = Categorie
        fields = '__all__'


class DetailCollecteSerializer:
    class Meta:
        model = DetailCollecte
        fields = '__all__'