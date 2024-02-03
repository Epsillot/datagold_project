
from django.contrib import admin

from .models import Client, Collecte, Categorie, DetailCollecte

admin.site.register(Client)
admin.site.register(Collecte)
admin.site.register(Categorie)
admin.site.register(DetailCollecte)