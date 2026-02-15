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
    def crear_asiento_completo(provider, fecha, descripcion, periodo, creado_por, transacciones_data):
        """
        Crea un asiento contable y sus transacciones de forma atómica.
        Valida que el asiento esté balanceado (débitos == créditos).

        :param provider: El perfil del prestador (inquilino).
        :param fecha: La fecha del asiento.
        :param descripcion: Descripción del asiento.
        :param periodo: El periodo contable al que pertenece.
        :param creado_por: El usuario que crea el asiento.
        :param transacciones_data: Una lista de diccionarios, cada uno representando una transacción.
                                 Ej: [{'cuenta_id': 1, 'debito': 100, 'credito': 0}, ...]
        """
        total_debito = sum(Decimal(t.get('debito', 0)) for t in transacciones_data)
        total_credito = sum(Decimal(t.get('credito', 0)) for t in transacciones_data)

        if total_debito != total_credito:
            raise ContabilidadValidationError(f"El asiento no está balanceado. Débitos: {total_debito}, Créditos: {total_credito}")

        if total_debito == 0:
            raise ContabilidadValidationError("El asiento debe tener un valor de débito y crédito mayor a cero.")

        try:
            with transaction.atomic():
                # Crear el asiento
                asiento = AsientoContable.objects.create(
                    provider=provider,
                    fecha=fecha,
                    descripcion=descripcion,
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
                        debito=Decimal(t_data.get('debito', 0)),
                        credito=Decimal(t_data.get('credito', 0)),
                        descripcion=t_data.get('descripcion', '')
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

            return {"status": "success", "message": f"El período {periodo.nombre} ha sido cerrado exitosamente."}

        except PeriodoContable.DoesNotExist:
            raise ContabilidadValidationError("El período no existe, ya está cerrado o no pertenece a tu negocio.")

    @staticmethod
    def obtener_libro_diario(provider, fecha_inicio, fecha_fin):
        """Genera el Libro Diario para un rango de fechas."""
        return AsientoContable.objects.filter(
            provider=provider,
            fecha__range=[fecha_inicio, fecha_fin]
        ).prefetch_related('transacciones', 'transacciones__cuenta').order_by('fecha', 'id')

    @staticmethod
    def obtener_libro_mayor(provider, cuenta_codigo, fecha_inicio, fecha_fin):
        """Genera los movimientos de una cuenta específica (Libro Mayor)."""
        return Transaccion.objects.filter(
            asiento__provider=provider,
            cuenta__codigo__startswith=cuenta_codigo,
            asiento__fecha__range=[fecha_inicio, fecha_fin]
        ).select_related('asiento', 'cuenta').order_by('asiento__fecha')

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
                total_debito=Sum('debito'),
                total_credito=Sum('credito')
            )

            debito = movimientos['total_debito'] or Decimal('0.00')
            credito = movimientos['total_credito'] or Decimal('0.00')

            if debito > 0 or credito > 0 or cuenta.saldo_inicial > 0:
                balance.append({
                    "codigo": cuenta.codigo,
                    "nombre": cuenta.nombre,
                    "saldo_inicial": cuenta.saldo_inicial,
                    "debitos": debito,
                    "creditos": credito,
                    "nuevo_saldo": cuenta.saldo_inicial + debito - credito
                })
        return balance

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
            nombre=f"Plan Contable Estándar - {provider.nombre_comercial}",
            defaults={"descripcion": "Plan de cuentas generado automáticamente por SARITA."}
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
        for codigo, nombre, tipo, parent_code in estructura:
            parent = cuentas_creadas.get(parent_code)
            cuenta, _ = Cuenta.objects.get_or_create(
                plan_de_cuentas=plan,
                codigo=codigo,
                defaults={
                    "nombre": nombre,
                    "tipo": tipo,
                    "parent": parent,
                    "provider": provider
                }
            )
            cuentas_creadas[codigo] = cuenta

        return plan
