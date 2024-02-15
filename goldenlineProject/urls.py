from django.contrib import admin
from django.urls import path, include
import authentication
from authentication import views
from datagold.views import PanierSocioProAPIView, DepenseMoyennePanierAPIView, Accueil, Moyenne, \
    CollecteAPIView, ClientAPIView


urlpatterns = [
    path('', authentication.views.login_page, name='login'),
    path('dashboard/', Accueil, name='index'),
    path('graph_moyenne', Moyenne),
    #path('api/client/', ClientAPIView.as_view()),
    path('admin/', admin.site.urls),
    #path('api/sociopro/', PanierSocioProAPIView.as_view(), name='paniersociopro'),
    #path('api/sociopromoyenne/', DepenseMoyennePanierAPIView.as_view(), name='sociopromoyenne'),
    path('api/collecte/', CollecteAPIView.as_view(), name='collecte'),
    path('logout/', authentication.views.logout_user, name='logout'),

]
