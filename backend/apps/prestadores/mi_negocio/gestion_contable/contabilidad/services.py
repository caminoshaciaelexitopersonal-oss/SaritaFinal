# backend/apps/prestadores/mi_negocio/gestion_contable/contabilidad/services.py
from decimal import Decimal
from django.db import transaction
from django.db.models import Sum
from .models import AsientoContable, Transaccion, Cuenta, PlanDeCuentas, PeriodoContable

class ContabilidadValidationError(Exception):
    """Excepción personalizada para errores de validación contable."""
    pass

class ContabilidadService:
    @staticmethod
    def crear_asiento_completo(provider, date, description, periodo, creado_por, transacciones_data):
        """
        Crea un asiento contable y sus transacciones de forma atómica.
        Valida que el asiento esté balanceado (débitos == créditos).

        :param provider: El perfil del prestador (inquilino).
        :param date: La date del asiento.
        :param description: Descripción del asiento.
        :param periodo: El periodo contable al que pertenece.
        :param creado_por: El usuario que crea el asiento.
        :param transacciones_data: Una lista de diccionarios, cada uno representando una transacción.
                                 Ej: [{'cuenta_id': 1, 'debit': 100, 'credit': 0}, ...]
        """
        total_debit = sum(Decimal(t.get('debit', 0)) for t in transacciones_data)
        total_credit = sum(Decimal(t.get('credit', 0)) for t in transacciones_data)

        if total_debit != total_credit:
            raise ContabilidadValidationError(f"El asiento no está balanceado. Débitos: {total_debit}, Créditos: {total_credit}")

        if total_debit == 0:
            raise ContabilidadValidationError("El asiento debe tener un valor de débito y crédito mayor a cero.")

        try:
            with transaction.atomic():
                # Crear el asiento
                asiento = AsientoContable.objects.create(
                    provider=provider,
                    date=date,
                    description=description,
                    periodo=periodo,
                    creado_por=creado_por
                )

                # Crear las transacciones
                for t_data in transacciones_data:
                    cuenta_id = t_data.get('cuenta_id')
                    cuenta = Cuenta.objects.get(id=cuenta_id, provider=provider) # Asegura que la cuenta pertenezca al inquilino

                    Transaccion.objects.create(
                        asiento=asiento,
                        cuenta=cuenta,
                        debit=Decimal(t_data.get('debit', 0)),
                        credit=Decimal(t_data.get('credit', 0)),
                        description=t_data.get('description', '')
                    )

            return asiento

        except Cuenta.DoesNotExist:
            raise ContabilidadValidationError("Una de las cuentas especificadas no existe o no pertenece a tu negocio.")
        except Exception as e:
            # Re-lanzar como una excepción de servicio para manejo en la capa superior (vista)
            raise ContabilidadValidationError(f"Error al crear el asiento: {str(e)}")

    @staticmethod
    def cerrar_periodo_contable(periodo_id, provider):
        """
        Marca un período contable como cerrado, impidiendo nuevos asientos.
        Aquí iría la lógica compleja de cálculo de saldos y asientos de cierre.

        (Función de esqueleto para desarrollo futuro)
        """
        try:
            periodo = PeriodoContable.objects.get(id=periodo_id, provider=provider, cerrado=False)

            # --- LÓGICA DE CIERRE (FUTURO) ---
            # 1. Validar que todos los asientos estén correctos.
            # 2. Calcular saldos finales de todas las cuentas.
            # 3. Generar asientos de cierre (ej. llevar cuentas de resultados a patrimonio).
            # 4. Actualizar saldos iniciales del siguiente período.
            # ------------------------------------

            periodo.cerrado = True
            periodo.save()

            return {"status": "success", "message": f"El período {periodo.name} ha sido cerrado exitosamente."}

        except PeriodoContable.DoesNotExist:
            raise ContabilidadValidationError("El período no existe, ya está cerrado o no pertenece a tu negocio.")

    @staticmethod
    def obtener_libro_diario(provider, start_date, end_date):
        """Genera el Libro Diario para un rango de fechas."""
        return AsientoContable.objects.filter(
            provider=provider,
            date__range=[start_date, end_date]
        ).prefetch_related('transactions', 'transactions__cuenta').order_by('date', 'id')

    @staticmethod
    def obtener_libro_mayor(provider, cuenta_code, start_date, end_date):
        """Genera los movimientos de una cuenta específica (Libro Mayor)."""
        return Transaccion.objects.filter(
            asiento__provider=provider,
            cuenta__code__startswith=cuenta_code,
            asiento__date__range=[start_date, end_date]
        ).select_related('asiento', 'cuenta').order_by('asiento__date')

    @staticmethod
    def generar_balance_comprobacion(provider, periodo_id):
        """Genera el Balance de Comprobación para un periodo."""
        cuentas = Cuenta.objects.filter(plan_de_cuentas__provider=provider)
        balance = []
        for cuenta in cuentas:
            movimientos = Transaccion.objects.filter(
                asiento__provider=provider,
                asiento__periodo_id=periodo_id,
                cuenta=cuenta
            ).aggregate(
                total_debit=Sum('debit'),
                total_credit=Sum('credit')
            )

            debit = movimientos['total_debit'] or Decimal('0.00')
            credit = movimientos['total_credit'] or Decimal('0.00')

            if debit > 0 or credit > 0 or cuenta.saldo_inicial > 0:
                balance.append({
                    "code": cuenta.code,
                    "name": cuenta.name,
                    "saldo_inicial": cuenta.saldo_inicial,
                    "debits": debit,
                    "credits": credit,
                    "nuevo_saldo": cuenta.saldo_inicial + debit - credit
                })
        return balance

    @staticmethod
    def generar_estado_resultados(provider, start_date, end_date):
        """
        Genera el Estado de Resultados (P&L): Ingresos - Gastos.
        """
        # Cuentas de Ingresos (Clase 4) y Gastos (Clase 5)
        cuentas_ingresos = Cuenta.objects.filter(provider=provider, code__startswith='4')
        cuentas_gastos = Cuenta.objects.filter(provider=provider, code__startswith='5')

        total_ingresos = Decimal('0.00')
        detalles_ingresos = []
        for c in cuentas_ingresos:
            val = Transaccion.objects.filter(
                asiento__provider=provider,
                asiento__date__range=[start_date, end_date],
                cuenta=c
            ).aggregate(saldo=Sum('credit') - Sum('debit'))['saldo'] or Decimal('0.00')
            if val != 0:
                total_ingresos += val
                detalles_ingresos.append({"cuenta": c.name, "valor": val})

        total_gastos = Decimal('0.00')
        detalles_gastos = []
        for c in cuentas_gastos:
            val = Transaccion.objects.filter(
                asiento__provider=provider,
                asiento__date__range=[start_date, end_date],
                cuenta=c
            ).aggregate(saldo=Sum('debit') - Sum('credit'))['saldo'] or Decimal('0.00')
            if val != 0:
                total_gastos += val
                detalles_gastos.append({"cuenta": c.name, "valor": val})

        return {
            "periodo": f"{start_date} a {end_date}",
            "ingresos": {"total": total_ingresos, "detalles": detalles_ingresos},
            "gastos": {"total": total_gastos, "detalles": detalles_gastos},
            "utilidad_neta": total_ingresos - total_gastos
        }

    @staticmethod
    def generar_balance_general(provider, cutoff_date):
        """
        Genera el Balance General: Activos = Pasivos + Patrimonio.
        """
        tipos = {
            "ACTIVO": '1',
            "PASIVO": '2',
            "PATRIMONIO": '3'
        }

        balance = {}
        total_secciones = {}

        for seccion, prefijo in tipos.items():
            cuentas = Cuenta.objects.filter(provider=provider, code__startswith=prefijo)
            total_seccion = Decimal('0.00')
            detalles = []

            for cuenta in cuentas:
                # El saldo acumulado incluye el saldo inicial + todos los movimientos hasta la fecha de corte
                movimientos = Transaccion.objects.filter(
                    asiento__provider=provider,
                    asiento__date__lte=cutoff_date,
                    cuenta=cuenta
                ).aggregate(d=Sum('debit'), c=Sum('credit'))

                deb = movimientos['d'] or Decimal('0.00')
                cre = movimientos['c'] or Decimal('0.00')

                # Regla de naturaleza de cuenta
                if prefijo == '1': # Activo: D - C
                    saldo = cuenta.saldo_inicial + deb - cre
                else: # Pasivo/Patrimonio: C - D
                    saldo = cuenta.saldo_inicial + cre - deb

                if saldo != 0:
                    total_seccion += saldo
                    detalles.append({"cuenta": cuenta.name, "code": cuenta.code, "saldo": saldo})

            balance[seccion] = detalles
            total_secciones[seccion] = total_seccion

        return {
            "cutoff_date": cutoff_date,
            "balance": balance,
            "totales": total_secciones,
            "diferencia_ecuacion": total_secciones["ACTIVO"] - (total_secciones["PASIVO"] + total_secciones["PATRIMONIO"])
        }

    @staticmethod
    def generar_flujo_caja(provider, start_date, end_date):
        """
        Genera un reporte de Flujo de Caja simplificado basado en cuentas de efectivo (Clase 11).
        """
        cuentas_efectivo = Cuenta.objects.filter(provider=provider, code__startswith='11')

        entradas = Transaccion.objects.filter(
            asiento__provider=provider,
            asiento__date__range=[start_date, end_date],
            cuenta__in=cuentas_efectivo,
            debit__gt=0
        ).aggregate(total=Sum('debit'))['total'] or Decimal('0.00')

        salidas = Transaccion.objects.filter(
            asiento__provider=provider,
            asiento__date__range=[start_date, end_date],
            cuenta__in=cuentas_efectivo,
            credit__gt=0
        ).aggregate(total=Sum('credit'))['total'] or Decimal('0.00')

        return {
            "periodo": f"{start_date} a {end_date}",
            "entradas_efectivo": entradas,
            "salidas_efectivo": salidas,
            "flujo_neto": entradas - salidas
        }

class StandardChartOfAccountsService:
    """
    Servicio para inicializar la estructura contable estándar de un nuevo prestador.
    """
    @staticmethod
    @transaction.atomic
    def inicializar_contabilidad(provider):
        # 1. Crear Plan de Cuentas
        plan, _ = PlanDeCuentas.objects.get_or_create(
            provider=provider,
            name=f"Plan Contable Estándar - {provider.name_comercial}",
            defaults={"description": "Plan de cuentas generado automáticamente por SARITA."}
        )

        # 2. Cuentas Maestras
        estructura = [
            # ACTIVOS
            ("1", "ACTIVOS", Cuenta.TipoCuenta.ACTIVO, None),
            ("11", "DISPONIBLE", Cuenta.TipoCuenta.ACTIVO, "1"),
            ("1105", "CAJA", Cuenta.TipoCuenta.ACTIVO, "11"),
            ("110505", "Caja General", Cuenta.TipoCuenta.ACTIVO, "1105"),
            ("1110", "BANCOS", Cuenta.TipoCuenta.ACTIVO, "11"),
            ("111005", "Moneda Nacional", Cuenta.TipoCuenta.ACTIVO, "1110"),
            ("1125", "PUENTE WALLET SARITA", Cuenta.TipoCuenta.ACTIVO, "11"),
            ("112505", "Wallet Soberano", Cuenta.TipoCuenta.ACTIVO, "1125"),

            # PASIVOS
            ("2", "PASIVOS", Cuenta.TipoCuenta.PASIVO, None),
            ("21", "OBLIGACIONES FINANCIERAS", Cuenta.TipoCuenta.PASIVO, "2"),
            ("23", "CUENTAS POR PAGAR", Cuenta.TipoCuenta.PASIVO, "2"),

            # PATRIMONIO
            ("3", "PATRIMONIO", Cuenta.TipoCuenta.PATRIMONIO, None),
            ("31", "CAPITAL SOCIAL", Cuenta.TipoCuenta.PATRIMONIO, "3"),

            # INGRESOS
            ("4", "INGRESOS", Cuenta.TipoCuenta.INGRESOS, None),
            ("41", "OPERACIONALES", Cuenta.TipoCuenta.INGRESOS, "4"),
            ("4135", "COMERCIO", Cuenta.TipoCuenta.INGRESOS, "41"),
            ("413505", "Servicios Turísticos", Cuenta.TipoCuenta.INGRESOS, "4135"),

            # GASTOS
            ("5", "GASTOS", Cuenta.TipoCuenta.GASTOS, None),
            ("51", "OPERACIONALES DE ADM", Cuenta.TipoCuenta.GASTOS, "5"),
            ("5105", "GASTOS DE PERSONAL", Cuenta.TipoCuenta.GASTOS, "51"),
        ]

        cuentas_creadas = {}
        for code, name, account_type, parent_code in estructura:
            parent = cuentas_creadas.get(parent_code)
            cuenta, _ = Cuenta.objects.get_or_create(
                plan_de_cuentas=plan,
                code=code,
                defaults={
                    "name": name,
                    "account_type": account_type,
                    "parent": parent,
                    "provider": provider
                }
            )
            cuentas_creadas[code] = cuenta

        return plan
