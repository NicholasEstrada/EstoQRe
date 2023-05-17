from django.http import HttpResponse

def teste(request):
    return HttpResponse("Ola Mundo do Janho.")

def teste2(request):
    return HttpResponse("Teste dois.")

