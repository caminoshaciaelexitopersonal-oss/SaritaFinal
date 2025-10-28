# backend/apps/activos/services.py
from datetime import date
from decimal import Decimal
from django.db import transaction
from .models import ActivoFijo, RegistroDepreciacion

@transaction.atomic
def depreciar_activo_un_mes(activo: ActivoFijo, fecha: date) -> RegistroDepreciacion | None:
    """
    Calcula, registra y actualiza la depreciación de un activo para un mes específico.
    Utiliza el método de línea recta.
    """
    if activo.valor_en_libros <= activo.valor_residual:
        return None # El activo ya está completamente depreciado

    # Evitar registrar depreciación para el mismo mes dos veces
    if RegistroDepreciacion.objects.filter(activo=activo, fecha__year=fecha.year, fecha__month=fecha.month).exists():
        return None

    base_depreciable = activo.costo_inicial - activo.valor_residual
    depreciacion_mensual = base_depreciable / activo.vida_util_meses

    # Ajustar si el último pago excede el valor en libros
    if (activo.valor_en_libros - depreciacion_mensual) < activo.valor_residual:
        depreciacion_mensual = activo.valor_en_libros - activo.valor_residual

    registro = RegistroDepreciacion.objects.create(
        activo=activo,
        fecha=fecha,
        monto=depreciacion_mensual
    )

    # Actualizar valores en el activo
    activo.depreciacion_acumulada += depreciacion_mensual
    activo.save() # .save() recalcula automáticamente el valor_en_libros

    return registro
