# backend/apps/contabilidad/services.py
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import JournalEntry, Transaction, ChartOfAccount

def create_full_journal_entry(
    perfil,
    date,
    description,
    transactions_data,
    created_by,
    cost_center=None
):
    """
    Crea un asiento contable completo con sus transacciones de forma atómica.
    Valida que los débitos y créditos totales sean iguales antes de guardar.

    Args:
        perfil (Perfil): El perfil del prestador al que pertenece el asiento.
        date (date): La fecha del asiento.
        description (str): Descripción general del asiento.
        transactions_data (list): Una lista de diccionarios, cada uno representando una transacción.
                                  Ej: [{'account_number': '110505', 'debit': 100, 'credit': 0}, ...]
        created_by (User): El usuario que crea el asiento.
        cost_center (CostCenter, optional): El centro de costo asociado.

    Returns:
        JournalEntry: La instancia del asiento contable creado.

    Raises:
        ValidationError: Si los débitos y créditos no cuadran o una cuenta no existe.
    """

    total_debit = sum(t.get('debit', 0) for t in transactions_data)
    total_credit = sum(t.get('credit', 0) for t in transactions_data)

    if total_debit != total_credit:
        raise ValidationError("El total de débitos y créditos debe ser igual.")

    if not transactions_data:
        raise ValidationError("Se requiere al menos una transacción.")

    with transaction.atomic():
        # Crear el asiento contable
        journal_entry = JournalEntry.objects.create(
            perfil=perfil,
            date=date,
            description=description,
            created_by=created_by,
            cost_center=cost_center
        )

        # Crear cada transacción
        transactions_to_create = []
        for t_data in transactions_data:
            account_number = t_data.get('account_number')
            try:
                # Se busca la cuenta dentro del plan de cuentas del perfil
                account = ChartOfAccount.objects.get(perfil=perfil, account_number=account_number)
            except ChartOfAccount.DoesNotExist:
                raise ValidationError(f"La cuenta contable '{account_number}' no existe para este perfil.")

            transactions_to_create.append(
                Transaction(
                    journal_entry=journal_entry,
                    account=account,
                    debit=t_data.get('debit', 0),
                    credit=t_data.get('credit', 0),
                    description=t_data.get('description', '')
                )
            )

        Transaction.objects.bulk_create(transactions_to_create)

        # Re-validar el asiento completo (aunque la lógica ya lo hace, es una doble verificación)
        journal_entry.full_clean()

    return journal_entry
