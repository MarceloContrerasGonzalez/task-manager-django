import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

#Creamos la clase pregunta con los atributos texto_pregunta y fecha_publicacion que son de tipo CharField y DateTimeField respectivamente
class pregunta(models.Model):
    texto_pregunta = models.CharField(max_length=200)#en este caso django no cuenta con StringField, por lo que se utiliza CharField con un max_length
    fecha_publicacion = models.DateTimeField("fecha de publicacion")#en este caso se utiliza DateTimeField para la fecha de publicacion

    ##Aqui se sobreescribe el metodo __str__ para que al imprimir un objeto de la clase pregunta se imprima el texto de la pregunta
    def __str__(self):
        return self.texto_pregunta

    ## creamos un metodo para verificar si la pregunta fue publicada recientemente
    def publicado_reciente(self):
        return self.fecha_publicacion >= timezone.now() - datetime.timedelta(days=1)

#Creamos la clase eleccion con los atributos pregunta, texto_eleccion y votos que son de tipo ForeignKey, CharField e IntegerField respectivamente
#de paso aqui haremos una relacion entre tablas para mostrar como se hace
class eleccion(models.Model):
    pregunta = models.ForeignKey(pregunta, on_delete=models.CASCADE) #on_delete=models.CASCADE significa que si se elimina la pregunta se eliminan todas las elecciones asociadas a ella
    texto_eleccion = models.CharField(max_length=200)
    votos = models.IntegerField(default=0) #en este caso se utiliza IntegerField para los votos ya que estos son numeros enteros y se inicializa en 0
    
    ##Aqui se sobreescribe el metodo __str__ para que al imprimir un objeto de la clase eleccion se imprima el texto de la eleccion
    def __str__(self):
        return self.texto_eleccion
    
    