from multiprocessing import context
from django.template import Template, Context

from django.http import HttpResponse




def plantilla(self):
    miHtml = open('/Users/federicofernandez/Desktop/MVT+FedericoF_ernandez/MVT/MVT/plantilla/template.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)

