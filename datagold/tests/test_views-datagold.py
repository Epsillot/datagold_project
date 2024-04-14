from datetime import date

import pytest
from django.contrib.auth.models import User
from django.test import RequestFactory
from datagold.models import Client, Collecte
from datagold.views import ClientAPIView, CollecteAPIView, PanierSocioProAPIView, DepenseMoyennePanierAPIView
from datagold.serializers import ClientSerializer
from rest_framework.response import Response

@pytest.fixture
def user():
    return User.objects.create_user(username='datapro', password='datapro')

@pytest.fixture
def client():
    return Client.objects.create(client_anonym='Client1', nombre_enfants=2, categorie_socioprofessionnelle='Catégorie2',
                          prix_panier_client=20.5, date=date.today(), collecte_achat=1)

@pytest.fixture
def collecte():
    return Collecte.objects.create(collecte=1, categorie_article='Catégorie1', prix_article=10)

@pytest.mark.django_db
def test_client_api_view(client, user):
    factory = RequestFactory()
    request = factory.get('/client-api/')
    request.user = user
    response = ClientAPIView.as_view()(request)
    assert response.status_code == 200
    assert len(response.data) == 1



@pytest.mark.django_db
def test_collecte_api_view(collecte, user):
    factory = RequestFactory()
    request = factory.get('/collecte-api/')
    request.user = user
    response = CollecteAPIView.as_view()(request)
    assert response.status_code == 200
    assert response.get('Content-Disposition') == 'attachment; filename="collectes.csv"'

@pytest.mark.django_db
def test_panier_socio_pro_api_view(client, user):
    factory = RequestFactory()
    request = factory.get('/panier-socio-pro-api/')
    request.user = user
    response = PanierSocioProAPIView.as_view()(request)
    assert response.status_code == 200

@pytest.mark.django_db
def test_depense_moyenne_panier_api_view(client, user):
    factory = RequestFactory()
    request = factory.get('/depense-moyenne-panier-api/')
    request.user = user
    response = DepenseMoyennePanierAPIView.as_view()(request)
    assert response.status_code == 200
