# backend/apps/contabilidad/services.py
from django.db import transaction as db_transaction
from decimal import Decimal
from .models import ChartOfAccount, JournalEntry, Transaction, CostCenter
from api.models import CustomUser as User # Adaptado al modelo de usuario del proyecto
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

# Se comentan las dependencias a módulos inexistentes
# from closing_process.models import ClosingPeriod
# from projects.models import Project

@db_transaction.atomic
def create_full_journal_entry(
    *, # Fuerza a que los argumentos se pasen por nombre
    user: User,
    perfil: Perfil,
    entry_date,
    description: str,
    entry_type: str,
    transactions_data: list
) -> JournalEntry:
    """
    Crea un asiento contable completo y sus transacciones de forma atómica y validada,
    asegurando que todos los datos pertenecen al perfil del prestador.
    """

    # --- 1. VALIDACIÓN DE PRE-CONDICIONES (GUARD CLAUSES) ---
    # La validación del período cerrado se implementará cuando exista el módulo `closing_process`
    # ...

    # --- 2. VALIDACIÓN DE LÓGICA DE NEGOCIO ---
    total_debits = sum(Decimal(t.get('debit', 0)) for t in transactions_data)
    total_credits = sum(Decimal(t.get('credit', 0)) for t in transactions_data)

    if total_debits != total_credits:
        raise ValueError(f"La partida doble no cuadra: Débitos={total_debits}, Créditos={total_credits}.")

    # --- 3. EJECUCIÓN ATÓMICA ---
    journal_entry = JournalEntry.objects.create(
        user=user,
        perfil=perfil, # Asignación del perfil
        entry_date=entry_date,
        description=description,
        entry_type=entry_type,
    )

    for tx_data in transactions_data:
        account_code = tx_data['account_code']
        try:
            # ROBUSTO: Se busca la cuenta dentro del perfil del prestador.
            account = ChartOfAccount.objects.get(code=account_code, perfil=perfil)
        except ChartOfAccount.DoesNotExist:
            raise ValueError(f"La cuenta contable '{account_code}' no existe para este negocio.")

        if not account.allows_transactions:
            raise ValueError(f"La cuenta de control '{account.code} - {account.name}' no permite transacciones.")

        cost_center = None
        if tx_data.get('cost_center_code'):
            try:
                # ROBUSTO: Se busca el centro de costo dentro del perfil del prestador.
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
