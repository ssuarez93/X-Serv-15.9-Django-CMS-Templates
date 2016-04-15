# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def profile(request):
    if request.method == "GET":
        if request.user.is_authenticated():
            respuesta = ("<h4>Eres " + request.user.username + ". " + '<a href="/logout">Logout</a></h4>')
            respuesta += "<p>Bienvenido, ya esta dentro de la pagina con su usuario.</p>"
        else:
            respuesta = ('Haz <a href="/login">login</a>')
    else:
        respuesta = "ERROR"
    return HttpResponse(respuesta)


@csrf_exempt
def identificador(request, ident):
    metodo = request.method
    if request.user.is_authenticated():
        respuesta = "Eres " + request.user.username + ". " + '<a href="/logout">Logout</a>'
    else:
        respuesta = '<p>Haz <a href="/login">login</a></p>'
    if metodo == "GET":
        try:
            pages = Pages.objects.get(id=int(ident))
            pagina = "<p>" +str(pages.page) + "</p>"
        except Pages.DoesNotExist:
            pagina = "<h4><p>Error. No hay pagina para el identificador introducido</p></h4>"
    else:
        pagina = "<h4><p>Error. Mediante un identificador solo se puede hacer GET de dicha pagina.</p></h4>"
    return HttpResponse(respuesta + pagina)


@csrf_exempt
def recurso(request, recurso):
    metodo = request.method
    pagina = " "
    if metodo == "GET":
        try:
            pages = Pages.objects.get(name=recurso)
            pagina = "<p>" +str(pages.page) + "</p>"
        except Pages.DoesNotExist:
            pagina = "<h4><p>Error. No hay pagina para el recurso introducido.</p></h4>"
    elif metodo == "PUT":
        if request.user.is_authenticated() == True:
            try:
                pages = Pages.objects.get(name=recurso)
                pagina = "<p>La pagina que usted quiere añadir ya esta en la lista de paginas. Compruebe antes.</p>"
            except Pages.DoesNotExist:
                cuerpo = request.body
                nueva = Pages(name=recurso, page=cuerpo)
                nueva.save()
                pagina = "<p>La pagina ha sido añadida.</p>"
        elif request.user.is_authenticated() == False:
            pagina = "Haz <a href='/login'>login</a> <p>Usted debe estar autentificado para dicha peticion.</p>"
    else:
        pagina = "<p>Ha ocurrido algun error. Solo se puede realizar GET o PUT.</p>"
    return HttpResponse(pagina)


def lista_paginas(request):
    respuesta = " "
    inicio = " "
    pagina = " "
    if request.user.is_authenticated():
        respuesta = ("Eres " + request.user.username + ". " + '<a href="/logout">Logout</a>')
    else:
        respuesta = ('Haz <a href="/login">login</a>')
    try:
        inicio = ("<h3><p>Lista de paginas almacenadas: </p></h3>")
        lista_pages = Pages.objects.all()
        pagina = ""
        for page in lista_pages:
            pagina += "<li><a href='/" + str(page.id) + "'>" + str(page.name) + "</a>"
    except Pages.DoesNotExist:
        pagina = ("<p>Ha ocurrido un error. No hay paginas almacenadas</p>")
    template = get_template('plantilla.html')
    return HttpResponse(template.render(Context({'login': respuesta, 'contenido': inicio + pagina})))


@csrf_exempt
def annotated_identificador(request, ident):
    metodo = request.method
    if request.user.is_authenticated():
        respuesta = "Eres " + request.user.username + ". " + '<a href="/logout">Logout</a>'
    else:
        respuesta = '<p>Haz <a href="/login">login</a></p>'
    if metodo == "GET":
        try:
            pages = Pages.objects.get(id=int(ident))
            pagina = "<p>" +str(pages.page) + "</p>"
        except Pages.DoesNotExist:
            pagina = "<h4><p>Error. No hay pagina para el identificador introducido</p></h4>"
    else:
        pagina = "<h4><p>Error. Mediante un identificador solo se puede hacer GET de dicha pagina.</p></h4>"

    template = get_template('plantilla.html')
    return HttpResponse(template.render(Context({'login': respuesta, 'pagina': pagina})))


@csrf_exempt
def annotated_recurso(request, recurso):
    metodo = request.method
    pagina = " "
    if metodo == "GET":
        try:
            pages = Pages.objects.get(name=recurso)
            pagina = "<p>" +str(pages.page) + "</p>"
        except Pages.DoesNotExist:
            pagina = "<h4><p>Error. No hay pagina para el recurso introducido.</p></h4>"
    elif metodo == "PUT":
        if request.user.is_authenticated() == True:
            try:
                pages = Pages.objects.get(name=recurso)
                pagina = "<p>La pagina que usted quiere añadir ya esta en la lista de paginas. Compruebe antes.</p>"
            except Pages.DoesNotExist:
                cuerpo = request.body
                nueva = Pages(name=recurso, page=cuerpo)
                nueva.save()
                pagina = "<p>La pagina ha sido añadida.</p>"
        elif request.user.is_authenticated() == False:
            pagina = "Haz <a href='/login'>login</a> <p>Usted debe estar autentificado para dicha peticion.</p>"
    else:
        pagina = "<p>Ha ocurrido algun error. Solo se puede realizar GET o PUT.</p>"
    template = get_template('plantilla.html')
    return HttpResponse(template.render(Context({'pagina': pagina})))
