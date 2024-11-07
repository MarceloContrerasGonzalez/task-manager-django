#Creamos un archivo llamado urls.py para la app polls para que se pueda acceder a la app desde la raiz del proyecto mysite
from django.urls import path

from . import views

# siempre que se cree una vista se debe importar en este archivo para que se pueda acceder a ella
# a la vez cada vez que se agregue un archivo urls.py en una app se debe importar en el archivo urls.py del proyecto (mysite/urls.py)
app_name = "polls" #se especifica el nombre de la app para que se pueda acceder a ella desde la raiz del proyecto
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"), 
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:pregunta_id>/vote/", views.vote, name="vote"),
    
]