import os
import django
from faker import Faker
from django.utils import timezone
from datetime import datetime, timedelta
import random
from django.db import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "goldenlineProject.settings")
django.setup()

from datagold.models import Collecte, Client

fake = Faker('fr_FR')

# Liste de catégories d'articles fictives
categories_articles = ['Électronique', 'Ménager', 'Informatique', 'Cuisine', 'Mode', 'Sport', 'Jouets', 'Beauté', 'Automobile']

# Liste de classes socioprofessionnelles
classes_socioprofessionnelles = ['Étudiant', 'Professionnel', 'Artisan', 'Cadre', 'Commerçant', 'Ouvrier', 'Retraité', 'Sans emploi', 'Indépendant']

# Générer des données pour la table Client
for i in range(1, 101):
    # Générer une date aléatoire dans l'année 2023
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = fake.date_between(start_date=start_date, end_date=end_date)

    # Générer un identifiant anonyme
    client_anonym = fake.uuid4()

    # Utiliser i pour collecte_achat dans la table Client
    Client.objects.create(
        client_anonym=client_anonym,
        nombre_enfants=max(0, fake.random_int(min=0, max=5)),
        categorie_socioprofessionnelle=random.choice(classes_socioprofessionnelles),
        prix_panier_client=max(0, fake.pydecimal(left_digits=5, right_digits=2, min_value=10, max_value=500)),
        date=random_date,
        collecte_achat=i
    )
# Générer des données pour la table Collecte
for _ in range(200):
    Collecte.objects.create(
        collecte=random.randint(1, 100),
        categorie_article=random.choice(categories_articles),
        prix_article=fake.pydecimal(left_digits=5, right_digits=2, min_value=10, max_value=500)
    )

    # Fonction pour mettre à jour prix_panier_client
    for client in Client.objects.all():
        # Calculer la somme des prix_article pour le collecte_achat actuel
        total_prix_article = Collecte.objects.filter(collecte=client.collecte_achat).aggregate(
            total_prix_article=models.Sum('prix_article'))['total_prix_article'] or 0
        client.prix_panier_client = total_prix_article
        client.save()


print("Données fictives générées avec succès.")