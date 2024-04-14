# generate_random_data.py
# python random_data_generator.py
# -*- coding: utf-8 -*-

import random
from faker import Faker
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# informations de connexion
DATABASE_URL = "postgresql://datapro:datapro@localhost:5432/datagold"
engine = create_engine(DATABASE_URL)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Client(Base):
    __tablename__ = 'datagold_client'
    id = Column(Integer, primary_key=True)
    nombre_enfants = Column(Integer)
    categorie_socioprofessionnelle = Column(String)


class Collecte(Base):
    __tablename__ = 'datagold_collecte'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    prix_panier_total = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)

fake = Faker('fr_FR')

def generate_random_data(num_clients=10, max_children=3, max_price=100):
    for _ in range(num_clients):
        client = Client(
            nombre_enfants=random.randint(0, max_children),
            categorie_socioprofessionnelle=fake.job(),
            prix_panier_client=random.randint(0, max_price)
        )
        session.add(client)
        session.flush()

        for _ in range(random.randint(1, 5)):  
            collecte = Collecte(
                client_id=client.id,
                prix_panier_total=random.randint(0, max_price)
            )
            session.add(collecte)

    session.commit()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    generate_random_data()
    print("Random data generated successfully.")


# Générer des données pour la table Collecte
collectes_achat = []  # Liste pour stocker les instances de Collecte pour collecte_achat

for i in range(1, 101):
    collecte_instance = Collecte.objects.create(
        collecte=i,
        categorie_article=random.choice(categories_articles),
        prix_article=max(0, fake.pydecimal(left_digits=5, right_digits=2))
    )
    collectes_achat.append(collecte_instance)
