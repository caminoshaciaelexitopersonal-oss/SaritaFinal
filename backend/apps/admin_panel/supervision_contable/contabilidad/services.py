from .models import ChartOfAccount

class ChartOfAccountService:
    def __init__(self, perfil):
        self.perfil = perfil

    def get_account(self, code_prefix):
        try:
            return ChartOfAccount.objects.get(perfil=self.perfil, code__startswith=code_prefix)
        except ChartOfAccount.DoesNotExist:
            raise Exception(f"Cuenta no encontrada con prefijo '{code_prefix}'.")
        except ChartOfAccount.MultipleObjectsReturned:
             return ChartOfAccount.objects.filter(perfil=self.perfil, code__startswith=code_prefix).first()

    def get_liability_account(self):
        return self.get_account('2')

    def get_expense_account(self):
        return self.get_account('5')
