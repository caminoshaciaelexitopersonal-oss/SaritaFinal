from decimal import Decimal
from django.db import transaction
from .models import Empleado, ConceptoNomina, Nomina, DetalleNomina
from apps.prestadores.models import Perfil
from datetime import date

@transaction.atomic
def procesar_nomina_service(perfil: Perfil, fecha_inicio: date, fecha_fin: date) -> Nomina:
    empleados_activos = Empleado.objects.filter(perfil=perfil, activo=True)
    if not empleados_activos.exists():
        raise ValueError("No se encontraron empleados activos para procesar la nómina.")
    conceptos = ConceptoNomina.objects.all()
    nomina = Nomina.objects.create(perfil=perfil, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, estado='procesada')
    total_ingresos_nomina = Decimal('0.00')
    total_deducciones_nomina = Decimal('0.00')
    for empleado in empleados_activos:
        total_ingresos_empleado = Decimal('0.00')
        total_deducciones_empleado = Decimal('0.00')
        salario_base = empleado.salario_base
        total_ingresos_empleado += salario_base
        for concepto in conceptos:
            valor_calculado = concepto.valor if concepto.es_fijo else salario_base * (concepto.valor or 0)
            DetalleNomina.objects.create(nomina=nomina, empleado=empleado, concepto=concepto, valor_calculado=valor_calculado)
            if concepto.tipo == 'ingreso':
                total_ingresos_empleado += valor_calculado
            elif concepto.tipo == 'deduccion':
                total_deducciones_empleado += valor_calculado
        total_ingresos_nomina += total_ingresos_empleado
        total_deducciones_nomina += total_deducciones_empleado
    nomina.total_ingresos = total_ingresos_nomina
    nomina.total_deducciones = total_deducciones_nomina
    nomina.neto_a_pagar = total_ingresos_nomina - total_deducciones_nomina
    nomina.save()
    return nomina
