import pytest
from datetime import date
from datagold.models import Collecte, Client

@pytest.mark.django_db
def test_collecte_model():
    Collecte.objects.create(collecte=1, categorie_article='Catégorie1', prix_article=10.5)
    collecte = Collecte.objects.get(pk=1)
    assert collecte.collecte == 1
    assert collecte.categorie_article == 'Catégorie1'
    assert collecte.prix_article == 10.5

@pytest.mark.django_db
def test_client_model():
    Client.objects.create(client_anonym='Client1', nombre_enfants=2, categorie_socioprofessionnelle='Catégorie2',
                          prix_panier_client=20.5, date=date.today(), collecte_achat=1)
    client = Client.objects.get(pk=1)
    assert client.client_anonym == 'Client1'
    assert client.nombre_enfants == 2
    assert client.categorie_socioprofessionnelle == 'Catégorie2'
    assert client.prix_panier_client == 20.5
    assert client.date == date.today()
    assert client.collecte_achat == 1
