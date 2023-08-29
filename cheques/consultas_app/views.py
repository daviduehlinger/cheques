from django.shortcuts import render
from consultas_app.models import Cheque

def consultar_cheques(request):
    cheques = Cheque.objects.all()
    context = {'cheques': cheques}
    return render(request, 'consulta_cheques.html', context)
