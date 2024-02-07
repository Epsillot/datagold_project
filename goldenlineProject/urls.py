
from django.contrib import admin
from django.urls import path, include

from datagold.views import ClientAPIView, PanierSocioProAPIView, DepenseMoyennePanierAPIView, Accueil, Moyenne, \
    CollecteAPIView

urlpatterns = [
    path('', Accueil, name='index'),
    path('graph_moyenne', Moyenne),
    path('admin/', admin.site.urls),
    path('api/client/', ClientAPIView.as_view()),
    path('api/sociopro/', PanierSocioProAPIView.as_view()),
    path('api/sociopromoyenne/', DepenseMoyennePanierAPIView.as_view(), name='sociopromoyenne'),
    path('api/collecte/', CollecteAPIView.as_view(), name='collecte')

]
