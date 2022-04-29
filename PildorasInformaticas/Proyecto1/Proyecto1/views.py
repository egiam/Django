from multiprocessing import context
from pipes import Template
from pydoc import doc
from xml.dom.minidom import Document
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):
    
    nombre = "Juan"
    apellido = "Diaz"
    ahora = datetime.datetime.now()

    p1 = Persona("Manuel", "Perez")

    # doc_externo = open("C:/Users/ezegi/OneDrive/Documentos/Educacion/Django/PildorasInformaticas/Proyecto1/Proyecto1/Plantillas/planSaludo.html")

    # plt = Template(doc_externo.read())

    # doc_externo.close()

    doc_externo = loader.get_template('planSaludo.html')

    # ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":["Plantillas","Modelos","Formularios","Vistas","Despliegue"]})

    documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":["Plantillas","Modelos","Formularios","Vistas","Despliegue"]})

    return HttpResponse(documento);

def despedida(request):
    return HttpResponse("Hasta luego!");


def dameFecha(request):
    fecha_actual = datetime.datetime.now();

    documento = """
    <html>
        <body>
            <h2>
                Fecha y hora actuales: %s
            </h2>
        </body>
    </html>
    """ % fecha_actual

    return HttpResponse(documento)


def calcularEdad(request, edad, agno):
    #edadActual = 18
    periodo = agno - 2019
    edadFutura = edad + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)

    return HttpResponse(documento)


