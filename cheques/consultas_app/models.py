from cheques_app.models import Cheque as ChequeOriginal

class Cheque(ChequeOriginal):
    class Meta:
        proxy = True