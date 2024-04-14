import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user_data():
    return {'username': 'datapro', 'password': 'datapro'}


@pytest.fixture
def create_user(db, user_data):
    return User.objects.create_user(**user_data)


def test_login_page_GET(client):
    response = client.get(reverse('login'))
    assert response.status_code == 200
    assert 'authentication/login.html' in [t.name for t in response.templates]


def test_login_page_POST_valid_credentials(client, user_data, create_user):
    response = client.post(reverse('login'), user_data)
    assert response.status_code == 302
    assert response.url == reverse('index')

@pytest.mark.django_db
def test_login_page_POST_invalid_credentials(client):
    response = client.post(reverse('login'), {'username': 'invalid_user', 'password': 'invalid_password'})
    assert response.status_code == 200
    assert 'authentication/login.html' in [t.name for t in response.templates]
    assert b'Identifiants invalides.' in response.content


def test_logout_user(client):
    response = client.get(reverse('logout'))
    assert response.status_code == 302
    assert response.url == reverse('login')
