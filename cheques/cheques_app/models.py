from django.db import models

class Banco(models.Model):
    banco_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)

class Cheque(models.Model):
    cheque_id = models.AutoField(primary_key=True)
    cheque_num = models.IntegerField()
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
