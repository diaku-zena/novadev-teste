from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from teste.forms import ContactoForm

from teste.models import Contacto # faz requisições HTTP


# Create your views here.


def index(request):
    api = "https://newsapi.org/v2/everything?q=tesla&from=2021-12-24&sortBy=publishedAt&apiKey=e5e9c11d31284e4aa521c73de74755a8"

    requisicao = requests.get(api)

    try:
        lista = requisicao.json()
    except ValueError:
        print("A resposta não chegou com o formato esperado.")

    item = {}
    titulos = {}
    autores = {}
    descricoes = {}
    imagens = {}

    for i in range(6):
        item["titulo"] = lista["articles"][i]["title"]
        item["autor"] = lista["articles"][i]["author"]
        item["descricao"] = lista["articles"][i]["description"]
        item["imagem"] = lista["articles"][i]["urlToImage"]
        titulos[i] = item["titulo"]
        autores[i] = item["autor"]
        descricoes[i] = item["descricao"]
        imagens[i] = item["imagem"]




    # Treating the form...

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('teste:contactos')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactoForm()
        print("Chegou aqui")

    contexto = {
        "titulos": titulos,
        "autores": autores,
        "descricoes": descricoes,
        "imagens": imagens,
        "form": form
    }


    return render(request, "index.html", contexto)

def contactos(request):
    # Mostra as mensagens
    mensagens = Contacto.objects.all()

    return render(request, 'contactos.html', {'mensagens': mensagens})