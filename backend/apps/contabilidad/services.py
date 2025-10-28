# backend/apps/contabilidad/services.py
from django.db import transaction as db_transaction
from decimal import Decimal
from .models import ChartOfAccount, JournalEntry, Transaction, CostCenter
from api.models import CustomUser as User # Adaptado al modelo de usuario del proyecto
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

@db_transaction.atomic
def create_full_journal_entry(
    *,
    user: User,
    perfil: Perfil,
    entry_date,
    description: str,
    entry_type: str,
    transactions_data: list,
    origin_document=None # <--- Argumento añadido
) -> JournalEntry:
    """
    Crea un asiento contable completo y sus transacciones de forma atómica y validada.
    """
    total_debits = sum(Decimal(t.get('debit', 0)) for t in transactions_data)
    total_credits = sum(Decimal(t.get('credit', 0)) for t in transactions_data)

    if total_debits != total_credits:
        raise ValueError(f"La partida doble no cuadra: Débitos={total_debits}, Créditos={total_credits}.")

    journal_entry = JournalEntry.objects.create(
        user=user,
        perfil=perfil,
        entry_date=entry_date,
        description=description,
        entry_type=entry_type,
        origin_document=origin_document # <--- Asignación del documento de origen
    )

    for tx_data in transactions_data:
        account_code = tx_data['account_code']
        try:
            account = ChartOfAccount.objects.get(code=account_code, perfil=perfil)
        except ChartOfAccount.DoesNotExist:
            raise ValueError(f"La cuenta contable '{account_code}' no existe para este negocio.")

        if not account.allows_transactions:
            raise ValueError(f"La cuenta de control '{account.code} - {account.name}' no permite transacciones.")

        cost_center = None
        if tx_data.get('cost_center_code'):
            try:
                cost_center = CostCenter.objects.get(code=tx_data['cost_center_code'], perfil=perfil)
            except CostCenter.DoesNotExist:
                 raise ValueError(f"El centro de costo '{tx_data.get('cost_center_code')}' no existe para este negocio.")

        Transaction.objects.create(
            journal_entry=journal_entry,
            account=account,
            debit=tx_data.get('debit', 0),
            credit=tx_data.get('credit', 0),
            cost_center=cost_center,
        )

    return journal_entry
