from django.shortcuts import render, redirect
from .models import Banco, Cliente, Cheque


def cargar_cheque(request):
    if request.method == 'POST':
        cheque_num = request.POST['cheque_num']
        banco_id = request.POST['banco']
        cliente_id = request.POST['cliente']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        monto = request.POST['monto']

        banco = Banco.objects.get(banco_id=banco_id)
        cliente = Cliente.objects.get(cliente_id=cliente_id)

        Cheque.objects.create(
            cheque_num=cheque_num,
            banco=banco,
            cliente=cliente,
            fecha_vencimiento=fecha_vencimiento,
            monto=monto
        )

        return redirect('confirmacion_cheque')

    bancos = Banco.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'cheques_form.html', {'bancos': bancos, 'clientes': clientes})


def confirmacion_cheque(request):
    return render(request, 'confirmation.html')