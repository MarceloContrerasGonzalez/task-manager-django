## en este archivo se registran los modelos para que puedan ser visualizados en el panel de administracion de django
#por esto vamos a registrar el modelo pregunta en el panel de administracion de django
from django.contrib import admin

from.models import pregunta

# Register your models here.
admin.site.register(pregunta)