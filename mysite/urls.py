#Este archivo es el archivo de configuracion de las urls de la aplicacion mysite
#es utilizado para redirigir las peticiones http a las vistas correspondientes

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #la funcion path requiere al menos dos argumentos: route y view
    path("polls/", include("polls.urls")), ## en esta linea incluimos las urls de la app polls para que se puedan acceder desde la raiz (mysite)
    path('admin/', admin.site.urls),
]
