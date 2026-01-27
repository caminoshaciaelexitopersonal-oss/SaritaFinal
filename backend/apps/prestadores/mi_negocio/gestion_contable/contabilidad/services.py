# backend/apps/prestadores/mi_negocio/gestion_contable/contabilidad/services.py
from decimal import Decimal
from django.db import transaction
from backend.models import AsientoContable, Transaccion, Cuenta

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

