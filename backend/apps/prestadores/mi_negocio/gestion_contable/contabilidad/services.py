from django.db import transaction as db_transaction
from decimal import Decimal
from .models import ChartOfAccount, JournalEntry, Transaction, CostCenter
# TODO: Importar Project cuando exista
# from apps.prestadores.mi_negocio.gestion_contable.proyectos.models import Project

# TODO: Importar ClosingPeriod cuando exista
# from close_process.models import ClosingPeriod

from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil
from api.models import CustomUser as User

@db_transaction.atomic
def create_full_journal_entry(
    *, # Force keyword-only arguments
    perfil: Perfil,
    user: User,
    entry_date,
    description: str,
    entry_type: str,
    transactions_data: list
) -> JournalEntry:
    """
    Crea un asiento contable completo y sus transacciones de forma atómica y validada.
    Este servicio es la ÚNICA forma segura de crear un asiento en el sistema.
    """

    # --- 1. VALIDACIÓN DE PRE-CONDICIONES ---
    # TODO: Implementar validación de período cerrado cuando el modelo ClosingPeriod exista.
    # is_period_closed = ClosingPeriod.objects.filter(
    #     perfil=perfil,
    #     period_year=entry_date.year,
    #     period_month=entry_date.month,
    #     status=ClosingPeriod.Status.CLOSED
    # ).exists()
    # if is_period_closed:
    #     raise ValueError(f"El período {entry_date.strftime('%Y-%m')} está cerrado.")

    # --- 2. VALIDACIÓN DE LÓGICA DE NEGOCIO ---
    total_debits = sum(Decimal(t.get('debit', 0)) for t in transactions_data)
    total_credits = sum(Decimal(t.get('credit', 0)) for t in transactions_data)

    if abs(total_debits - total_credits) > Decimal('0.01'):
        raise ValueError(f"La partida doble no cuadra: Débitos={total_debits}, Créditos={total_credits}.")

    # --- 3. EJECUCIÓN ATÓMICA ---
    journal_entry = JournalEntry.objects.create(
        perfil=perfil,
        user=user,
        entry_date=entry_date,
        description=description,
        entry_type=entry_type,
    )

    for tx_data in transactions_data:
        account_code = tx_data['account_code']
        try:
            account = ChartOfAccount.objects.get(code=account_code)
        except ChartOfAccount.DoesNotExist:
            raise ValueError(f"La cuenta contable '{account_code}' no existe.")

        if not account.allows_transactions:
            raise ValueError(f"La cuenta de control '{account.code} - {account.name}' no permite transacciones.")

        # Obtener dimensiones (proyecto, centro de costo) si existen
        cost_center = None
        # project = None # TODO: Habilitar cuando exista el modelo Project

        if tx_data.get('cost_center_code'):
            cost_center = CostCenter.objects.get(code=tx_data['cost_center_code'], perfil=perfil)

        # if tx_data.get('project_code'):
        #     project = Project.objects.get(code=tx_data['project_code'], perfil=perfil)

        Transaction.objects.create(
            journal_entry=journal_entry,
            account=account,
            debit=tx_data.get('debit', 0),
            credit=tx_data.get('credit', 0),
            cost_center=cost_center,
            # project=project, # TODO: Habilitar
        )

    return journal_entry
