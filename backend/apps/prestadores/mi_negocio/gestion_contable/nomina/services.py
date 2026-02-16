from decimal import Decimal, ROUND_HALF_UP
from django.db import transaction, models
from django.utils import timezone
from .models import (
    Empleado, Contrato, Planilla, DetalleLiquidacion,
    NovedadNomina, IncapacidadLaboral, ProvisionNomina, IndicadorLaboral
)
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import AsientoContable, Transaccion, Cuenta, PeriodoContable
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.services import ContabilidadService

class NominaService:
    """
    Motor Central de Nómina SARITA.
    Maneja liquidación, provisiones e integración contable.
    """

    @staticmethod
    @transaction.atomic
    def liquidar_periodo(planilla_id, usuario_id=None):
        planilla = Planilla.objects.select_for_update().get(id=planilla_id)

        # 1. Blindaje de Estado
        if planilla.estado != Planilla.EstadoPlanilla.BORRADOR:
            raise ValueError(f"Blindaje Activo: La planilla {planilla_id} ya fue liquidada/cerrada.")

        # 2. Blindaje de Periodo Contable
        periodo = PeriodoContable.objects.filter(
            provider=planilla.perfil,
            fecha_inicio__lte=planilla.periodo_inicio,
            fecha_fin__gte=planilla.periodo_fin,
            cerrado=False
        ).first()
        if not periodo:
            raise ValueError("Acción Bloqueada: No existe un período contable abierto para estas fechas.")

        # Limpiar liquidaciones previas si existen
        planilla.detalles_liquidacion.all().delete()

        empleados = Empleado.objects.filter(perfil=planilla.perfil, estado=Empleado.EstadoEmpleado.ACTIVO)

        total_dev = Decimal('0.00')
        total_ded = Decimal('0.00')

        for emp in empleados:
            contrato = emp.contratos.filter(activo=True).first()
            if not contrato: continue

            # Cálculo Base (Simplificado para Fase 8 Structural)
            # En un sistema real, esto consideraría el IBC y leyes específicas (Colombia en este caso)
            salario_base = contrato.salario
            dias = 30 # Asumimos mes comercial

            # Devengados
            basico = salario_base
            aux_transporte = Decimal('140606.00') if salario_base <= (1300000 * 2) else Decimal('0.00') # Ejemplo SMMLV 2024 aprox

            # Novedades (Horas extras, bonos, etc.)
            novedades = NovedadNomina.objects.filter(empleado=emp, planilla=planilla, procesada=False)
            extra_dev = sum(n.valor for n in novedades if n.concepto.tipo == 'DEVENGADO')
            extra_ded = sum(n.valor for n in novedades if n.concepto.tipo == 'DEDUCCION')

            # Deducciones de Ley (Colombia: 4% Salud, 4% Pensión)
            salud = (basico * Decimal('0.04')).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
            pension = (basico * Decimal('0.04')).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)

            total_emp_dev = basico + aux_transporte + extra_dev
            total_emp_ded = salud + pension + extra_ded
            neto = total_emp_dev - total_emp_ded

            # Prestaciones y Aportes Patronales (Causación)
            prima = (total_emp_dev * Decimal('0.0833')).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
            cesantias = (total_emp_dev * Decimal('0.0833')).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
            int_cesantias = (cesantias * Decimal('0.12')).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
            vacaciones = (basico * Decimal('0.0417')).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)

            # Aportes Patronales
            salud_patron = (basico * Decimal('0.085')).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
            pension_patron = (basico * Decimal('0.12')).quantize(Decimal('1.'), rounding=ROUND_HALF_UP)
            arl = (basico * Decimal('0.00522')).quantize(Decimal('1.'), rounding=ROUND_HALF_UP) # Nivel 1

            detalle = DetalleLiquidacion.objects.create(
                planilla=planilla,
                empleado=emp,
                salario_base=salario_base,
                dias_trabajados=dias,
                basico=basico,
                auxilio_transporte=aux_transporte,
                total_devengado=total_emp_dev,
                salud_empleado=salud,
                pension_empleado=pension,
                total_deduccion=total_emp_ded,
                total_neto=neto,
                valor_prima=prima,
                valor_cesantias=cesantias,
                valor_intereses_cesantias=int_cesantias,
                valor_vacaciones=vacaciones,
                valor_aporte_salud_patron=salud_patron,
                valor_aporte_pension_patron=pension_patron,
                valor_aporte_arl=arl
            )

            total_dev += total_emp_dev
            total_ded += total_emp_ded

            # Marcar novedades como procesadas
            novedades.update(procesada=True)

        planilla.total_devengado = total_dev
        planilla.total_deduccion = total_ded
        planilla.total_neto = total_dev - total_ded
        planilla.estado = Planilla.EstadoPlanilla.LIQUIDADA
        planilla.save()

        return planilla

    @staticmethod
    @transaction.atomic
    def contabilizar_nomina(planilla_id, usuario_id=None):
        planilla = Planilla.objects.select_for_update().get(id=planilla_id)

        # 1. Idempotencia: Evitar duplicidad de asientos
        if planilla.asiento_contable_ref_id:
            raise ValueError(f"Idempotencia Activa: La planilla {planilla_id} ya tiene un asiento contable (Ref: {planilla.asiento_contable_ref_id}).")

        if planilla.estado != Planilla.EstadoPlanilla.LIQUIDADA:
            raise ValueError("Solo se pueden contabilizar planillas en estado LIQUIDADA.")

        # Buscar periodo contable
        periodo = PeriodoContable.objects.filter(
            provider=planilla.perfil,
            fecha_inicio__lte=planilla.periodo_inicio,
            fecha_fin__gte=planilla.periodo_fin,
            cerrado=False
        ).first()

        if not periodo:
            raise ValueError("No existe un período contable abierto para las fechas de la planilla.")

        # Crear Asiento
        asiento = AsientoContable.objects.create(
            provider=planilla.perfil,
            periodo=periodo,
            fecha=timezone.now().date(),
            descripcion=f"CAUSACION NOMINA PERIODO {planilla.periodo_inicio} - {planilla.periodo_fin}",
            creado_por_id=usuario_id
        )

        # Aquí vendría la lógica de mapeo de cuentas.
        # Para esta fase structural, buscaremos o crearemos cuentas por defecto.
        # En una implementación real, esto lo define el Plan de Cuentas del Tenant.

        def get_cuenta(codigo, nombre, tipo):
            plan = planilla.perfil.plandecuentas_items.first()
            cuenta, _ = Cuenta.objects.get_or_create(
                plan_de_cuentas=plan,
                codigo=codigo,
                defaults={'nombre': nombre, 'tipo': tipo, 'provider': planilla.perfil}
            )
            return cuenta

        c_gasto_sueldos = get_cuenta("510506", "Sueldos Básicos", "GASTOS")
        c_gasto_transp = get_cuenta("510527", "Auxilio de Transporte", "GASTOS")
        c_pasivo_nomina = get_cuenta("250505", "Salarios por Pagar", "PASIVO")
        c_pasivo_salud = get_cuenta("237005", "Aportes a Salud", "PASIVO")
        c_pasivo_pension = get_cuenta("238030", "Aportes a Pensión", "PASIVO")

        # 1. Registrar Gasto Sueldos (Debito)
        Transaccion.objects.create(asiento=asiento, cuenta=c_gasto_sueldos, debito=planilla.total_devengado, descripcion="Gasto Nómina")

        # 2. Registrar Deducciones (Credito)
        detalles = planilla.detalles_liquidacion.all()
        t_salud = sum(d.salud_empleado for d in detalles)
        t_pension = sum(d.pension_empleado for d in detalles)

        Transaccion.objects.create(asiento=asiento, cuenta=c_pasivo_salud, credito=t_salud, descripcion="Retención Salud")
        Transaccion.objects.create(asiento=asiento, cuenta=c_pasivo_pension, credito=t_pension, descripcion="Retención Pensión")

        # 3. Salarios por Pagar (Credito)
        Transaccion.objects.create(asiento=asiento, cuenta=c_pasivo_nomina, credito=planilla.total_neto, descripcion="Neto a Pagar")

        # El asiento debe balancear: Debitos = Creditos
        # Total Debito = planilla.total_devengado
        # Total Credito = t_salud + t_pension + planilla.total_neto = total_deduccion + neto = total_devengado

        planilla.estado = Planilla.EstadoPlanilla.CONTABILIZADA
        planilla.asiento_contable_ref_id = asiento.id
        planilla.save()

        return asiento

    @staticmethod
    def generar_indicadores(provider_id):
        provider = ProviderProfile.objects.get(id=provider_id)
        # Costo Laboral Total
        total_costo = DetalleLiquidacion.objects.filter(planilla__perfil=provider).aggregate(s=models.Sum('total_devengado'))['s'] or 0

        IndicadorLaboral.objects.create(
            perfil=provider,
            nombre="Costo Laboral Total",
            valor=total_costo,
            periodo=timezone.now().strftime("%Y-%m")
        )
        return True

    @staticmethod
    @transaction.atomic
    def liquidar_contrato(contrato_id, fecha_retiro, motivo, usuario_id=None):
        """
        Realiza la liquidación final de un contrato laboral.
        """
        contrato = Contrato.objects.select_for_update().get(id=contrato_id)
        if not contrato.activo:
            raise ValueError("El contrato ya está liquidado/inactivo.")

        # Marcar contrato como inactivo
        contrato.fecha_fin = fecha_retiro
        contrato.activo = False
        contrato.save()

        # Actualizar estado del empleado
        empleado = contrato.empleado
        empleado.estado = Empleado.EstadoEmpleado.RETIRADO
        empleado.save()

        # En una implementación real, se generaría un Asiento Contable por el pago de prestaciones.
        return True
