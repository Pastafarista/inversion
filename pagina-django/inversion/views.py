from obtener_grafica import obtener_grafica
from django.http import HttpResponse
from django.template import Template, Context
import os

def ver_grafica(request):

    #Ruta de la carpeta donde se encuentra el archivo html
    ruta = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(ruta, "plantillas/grafica.html")
    
    doc_externo = open(ruta)
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context({"graph": obtener_grafica()})
    
    documento = plt.render(ctx)
    
    return HttpResponse(documento)
