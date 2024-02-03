
from django.contrib import admin
from django.urls import path, include

from datagold.views import ClientAPIView, PanierSocioProAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/client/', ClientAPIView.as_view()),
    path('api/sociopro/', PanierSocioProAPIView.as_view())
]
