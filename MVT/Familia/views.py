from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from Familia.models import Familia
from django.template import loader, Template




def papa(self):
    papa = Familia( nombre = "Luis", apellido = "Fernandez", dni = 11200200, telefono = 4656565, fechaDeNacimiento = "1963-05-08")
    papa.save()
    documentoPapa = f"Nombre:{papa.nombre} - Apellido:{papa.apellido} - Dni:{papa.dni} - Telefono:{papa.telefono} - Fecha De Nacimiento:{papa.fechaDeNacimiento}"
    return HttpResponse(documentoPapa)

def mama(self):
    mama = Familia(nombre = "Viviana", apellido = "San Felipe", dni = 12543897, telefono = 4242424, fechaDeNacimiento = "1955-10-15")
    mama.save()
    documentoMama = f"Nombre:{mama.nombre} - Apellido:{mama.apellido} - Dni:{mama.dni} - Telefono:{mama.telefono} - Fecha de Nacimiento:{mama.fechaDeNacimiento}"
    return HttpResponse(documentoMama)

def hermana(self):
    hermana1 = Familia(nombre = "Lorena", apellido = "Fernandez", dni = 29987654, telefono = 351378199, fechaDeNacimiento = "1983-06-18")
    hermana1.save()
    documentoHermana1 = f"Nombre:{hermana1.nombre} - Apellido:{hermana1.apellido} - Dni:{hermana1.dni} - Telefono:{hermana1.telefono} - Fecha de Nacimiento:{hermana1.fechaDeNacimiento}"
    return HttpResponse(documentoHermana1)






