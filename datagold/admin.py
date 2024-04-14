from django.contrib import admin
from datagold.models import Client, Collecte
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class ClientAdmin(admin.ModelAdmin):
    list_display   = ('client_anonym', 'nombre_enfants', 'categorie_socioprofessionnelle', 'prix_panier_client', 'date', 'collecte_achat')
    list_filter    = ('categorie_socioprofessionnelle','prix_panier_client', )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('categorie_socioprofessionnelle', 'date')



class CollectAdmin(admin.ModelAdmin):
    list_display   = ('collecte', 'categorie_article', 'prix_article')
    list_filter    = ('categorie_article','prix_article', )

    ordering       = ('collecte', )
    search_fields  = ('categorie_article', 'prix_article')


admin.site.register(Client, ClientAdmin)
admin.site.register(Collecte, CollectAdmin)

admin.site.site_title = _('DataGold admin')
admin.site.site_header = _('DataGold administration')
admin.site.index_title = _('Administration de DataGold')