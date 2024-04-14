from django.contrib import admin
from django.urls import path, include
from authentication import views as auth_views
from datagold.views import PanierSocioProAPIView, DepenseMoyennePanierAPIView, Accueil, Moyenne, \
    CollecteAPIView, ClientAPIView
from django.conf.urls import handler404, handler500


handler404 = 'authentication.views.custom_page_not_found'
handler500 = 'authentication.views.custom_server_error'

urlpatterns = [
    path('login/', auth_views.login_page,  name='login'),
    path('dashboard/', Accueil, name='index'),
    path('graph_moyenne/', Moyenne, name='Moyenne'),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api/collecte/', CollecteAPIView.as_view(), name='collecte'),
    path('logout/', auth_views.logout_user, name='logout'),



]
