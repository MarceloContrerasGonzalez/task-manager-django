#Creamos un archivo llamado urls.py para la app polls para que se pueda acceder a la app desde la raiz del proyecto mysite
from django.urls import path
from . import views

# siempre que se cree una vista se debe importar en este archivo para que se pueda acceder a ella
# a la vez cada vez que se agregue un archivo urls.py en una app se debe importar en el archivo urls.py del proyecto (mysite/urls.py)
app_name = 'polls' #se especifica el nombre de la app para que se pueda acceder a ella desde la raiz del proyecto
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:pregunta_id>/', views.detail, name='detail'), #se especifica views.detail para que se pueda acceder a la vista detail tiene que tener el mismo nombre que la vista
    # ex: /polls/5/results/
    path('<int:pregunta_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:pregunta_id>/vote/', views.vote, name='vote'),
    
]