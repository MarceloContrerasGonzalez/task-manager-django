#from django.http import HttpResponse
#from django.template import loader
#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import pregunta as Pregunta ##marco Pregunta con mayuscula para que sea mas facil de identificar
# Create your views here.

def index(request):
    #se obtienen las ultimas 5 preguntas y se las ordena por fecha de publicacion
    latest_question_list = Pregunta.objects.order_by('-fecha_publicacion')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/index.html", context)


#se crea una vista para mostrar el detalle de una pregunta
def detail(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request, "polls/detail.html", {'pregunta': pregunta})
        

#se crea una vista para mostrar los resultados de una pregunta
def results(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request, "polls/results.html", {'pregunta': pregunta})

#se crea una vista para votar en una pregunta
def vote(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request, "polls/vote.html", {'pregunta': pregunta})