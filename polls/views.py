#from django.template import loader ##se importa loader para poder cargar un template pero en vez de usar loader usare render
#from django.http import Http404 ##se importa Http404 para poder lanzar un error 404 pero en vez de usar Http404 usare get_object_or_404
from django.db.models import F ##se importa F para poder hacer consultas en la base de datos
from django.http import HttpResponseRedirect ##se importa HttpResponseRedirect para poder redirigir a una vista en especifico
from django.shortcuts import get_object_or_404, render
from django.urls import reverse ##se importa reverse para poder redirigir a una vista en especifico
from django.views import generic

from .models import eleccion as Eleccion ##marco eleccion con mayuscula para que sea mas facil de identificar
from .models import pregunta as Pregunta ##marco Pregunta con mayuscula para que sea mas facil de identificar
# Create your views here.

#se crea una vista para mostrar las preguntas
class IndexView(generic.ListView):
    template_name = "polls/index.html" ##se especifica el template que se va a utilizar o django usara uno por defecto llamado <nombre_app>/<nombre_modelo>_list.html
    context_object_name = "latest_question_list"

    def get_queryset(self): ##se sobreescribe el metodo get_queryset para devolver las ultimas 5 preguntas publicadas sino se sobreescribe se devolveran todas las preguntas
        #retorna las ultimas 5 preguntas publicadas
        return Pregunta.objects.order_by("-fecha_publicacion")[:5]

#se crea una vista para mostrar los detalles de una pregunta
class DetailView(generic.DetailView):
    model = Pregunta #esto generara una variable de contexto llamada pregunta permitiendo acceder a los datos del modelo pregunta
    template_name = "polls/detail.html"

#se crea una vista para mostrar los resultados de una pregunta
class ResultsView(generic.DetailView):
    model = Pregunta
    template_name = "polls/results.html"

#se crea una vista para votar en una pregunta
def vote(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        selected_choice = pregunta.eleccion_set.get(pk=request.POST['eleccion'])
    except (KeyError, Eleccion.DoesNotExist):
        # mostramos el formulario de votacion de nuevo
        return render(
            request,
            "polls/detail.html",
            {
                "pregunta": pregunta,
                "error_message": "no seleccionaste ninguna opcion",
            },
        )
    else:
        selected_choice.votos = F("votos") + 1
        selected_choice.save()
        #siempre se debe retornar un HttpResponseRedirect despues de procesar un formulario con exito utilizando POST
        #esto previene que los datos se envien dos veces si el usuario presiona el boton de regresar
    return HttpResponseRedirect(reverse("polls:results", args=(pregunta.id,)))