from rest_framework.serializers import ModelSerializer

from datagold.models import Client, Collecte

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CollecteSerializer:
    class Meta:
        model = Collecte
        fields = '__all__'


