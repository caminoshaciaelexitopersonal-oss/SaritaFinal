# backend/apps/prestadores/mi_negocio/gestion_contable/contabilidad/management/commands/load_puc.py
from django.core.management.base import BaseCommand
from ...models import PlanDeCuentas, Cuenta
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile

class Command(BaseCommand):
    help = 'Loads a standard Chart of Accounts (PUC)'

    def handle(self, *args, **options):
        self.stdout.write("Cargando Plan de Cuentas Maestro...")

        perfil = ProviderProfile.objects.first()
        if not perfil:
            self.stdout.write(self.style.ERROR("No se encontró un perfil de prestador para asociar el PUC."))
            return

        puc, _ = PlanDeCuentas.objects.get_or_create(
            provider=perfil,
            nombre="PUC Comercial Estándar",
            defaults={"descripcion": "Plan Único de Cuentas para prestadores de servicios turísticos."}
        )

        # Cuentas principales
        cuentas = [
            ("1", "ACTIVOS", "ACTIVO", None),
            ("11", "DISPONIBLE", "ACTIVO", "1"),
            ("1105", "CAJA", "ACTIVO", "11"),
            ("1110", "BANCOS", "ACTIVO", "11"),
            ("4", "INGRESOS", "INGRESOS", None),
            ("41", "OPERACIONALES", "INGRESOS", "4"),
            ("4135", "COMERCIO", "INGRESOS", "41"),
            ("2", "PASIVOS", "PASIVO", None),
            ("24", "IMPUESTOS", "PASIVO", "2"),
            ("2408", "IVA POR PAGAR", "PASIVO", "24"),
        ]

        for codigo, nombre, tipo, parent_code in cuentas:
            parent = Cuenta.objects.filter(plan_de_cuentas=puc, codigo=parent_code).first() if parent_code else None
            Cuenta.objects.get_or_create(
                plan_de_cuentas=puc,
                codigo=codigo,
                defaults={
                    "nombre": nombre,
                    "tipo": tipo,
                    "parent": parent,
                    "provider": perfil
                }
            )

        self.stdout.write(self.style.SUCCESS(f"PUC cargado exitosamente para {perfil.nombre_comercial}"))
