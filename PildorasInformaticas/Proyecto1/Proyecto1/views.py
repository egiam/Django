from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola, mi primera pagina con Django.");

def despedida(request):
    return HttpResponse("Hasta luego!");




