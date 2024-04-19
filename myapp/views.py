from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Pessoa

def agendamento(request):
    return render(request, 'agendamento.html')

def agendados(request):
    pessoa_agendados = Pessoa()
    pessoa_agendados.nome = request.POST.get('nome')
    pessoa_agendados.cpf = request.POST.get('cpf')
    pessoa_agendados.data = request.POST.get('data')
    pessoa_agendados.especialidade = request.POST.get('especialidade')
    pessoa_agendados.save()

    return render (request, 'agendados.html')

def json(request):
    data=list(Pessoa.objects.values())
    return JsonResponse(data, safe=False)
