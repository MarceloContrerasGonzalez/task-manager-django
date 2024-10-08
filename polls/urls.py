#Creamos un archivo llamado urls.py para la app polls para que se pueda acceder a la app desde la raiz del proyecto mysite
from django.urls import path
from . import views

# siempre que se cree una vista se debe importar en este archivo para que se pueda acceder a ella
# a la vez cada vez que se agregue un archivo urls.py en una app se debe importar en el archivo urls.py del proyecto (mysite/urls.py)
urlpatterns = [
    path('', views.index, name='index'),
]