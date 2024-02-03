
from django.contrib import admin
from django.urls import path, include

from datagold.views import ClientAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/client/', ClientAPIView.as_view())
]
