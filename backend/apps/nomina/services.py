from decimal import Decimal
from django.db import transaction
from .models import Empleado, ConceptoNomina, Nomina, DetalleNomina
from apps.prestadores.models import Perfil
from datetime import date

@transaction.atomic
def procesar_nomina_service(perfil: Perfil, fecha_inicio: date, fecha_fin: date) -> Nomina:
    """
    Servicio para procesar una corrida de nómina para un prestador en un período específico.

    Args:
        perfil (Perfil): El perfil del prestador para el cual se procesa la nómina.
        fecha_inicio (date): Fecha de inicio del período de la nómina.
        fecha_fin (date): Fecha de fin del período de la nómina.

    Returns:
        Nomina: La instancia de la nómina recién procesada.

    Raises:
        ValueError: Si no hay empleados activos para procesar.
    """

    # 1. Obtener empleados activos y conceptos de nómina
    empleados_activos = Empleado.objects.filter(perfil=perfil, activo=True)
    if not empleados_activos.exists():
        raise ValueError("No se encontraron empleados activos para procesar la nómina.")

    conceptos = ConceptoNomina.objects.all()

    # 2. Crear la cabecera de la nómina
    nomina = Nomina.objects.create(
        perfil=perfil,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        estado='procesada'  # Se marca como procesada al final
    )

    total_ingresos_nomina = Decimal('0.00')
    total_deducciones_nomina = Decimal('0.00')

    # 3. Iterar sobre cada empleado para calcular su nómina
    for empleado in empleados_activos:
        total_ingresos_empleado = Decimal('0.00')
        total_deducciones_empleado = Decimal('0.00')

        # Primero, procesar el salario base como un ingreso
        salario_base = empleado.salario_base
        total_ingresos_empleado += salario_base

        # Opcional: Podríamos tener un concepto específico para 'SALARIO_BASE'
        # y registrarlo como un detalle. Por simplicidad, lo tratamos como punto de partida.

        # 4. Iterar sobre cada concepto para calcular su valor
        for concepto in conceptos:
            valor_calculado = Decimal('0.00')

            if concepto.es_fijo:
                valor_calculado = concepto.valor or Decimal('0.00')
            else: # Es un porcentaje
                porcentaje = concepto.valor or Decimal('0.00')
                valor_calculado = salario_base * porcentaje

            # Crear el registro de detalle
            DetalleNomina.objects.create(
                nomina=nomina,
                empleado=empleado,
                concepto=concepto,
                valor_calculado=valor_calculado
            )

            # Acumular en los totales del empleado
            if concepto.tipo == 'ingreso':
                total_ingresos_empleado += valor_calculado
            elif concepto.tipo == 'deduccion':
                total_deducciones_empleado += valor_calculado

        # Acumular en los totales de la nómina
        total_ingresos_nomina += total_ingresos_empleado
        total_deducciones_nomina += total_deducciones_empleado

    # 5. Guardar los totales calculados en la instancia de la nómina
    nomina.total_ingresos = total_ingresos_nomina
    nomina.total_deducciones = total_deducciones_nomina
    nomina.neto_a_pagar = total_ingresos_nomina - total_deducciones_nomina
    nomina.save()

    return nomina
