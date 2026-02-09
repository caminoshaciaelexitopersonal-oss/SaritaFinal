from django.core.management.base import BaseCommand
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
from apps.sarita_agents.agents.general.sarita.coroneles.comercial.capitanes.capitan_marketing import CapitanMarketing
from apps.sarita_agents.agents.general.sarita.coroneles.comercial.tenientes.teniente_marketing import TenienteMarketing
from apps.sarita_agents.agents.general.sarita.coroneles.comercial.sargentos.sargento_marketing import SargentoMarketing
from apps.sarita_agents.agents.general.sarita.coroneles.comercial.soldados.soldado_marketing_1 import SoldadoMarketing1

class Command(BaseCommand):
    help = 'Ejecuta la Prueba de Realidad de la Fase 1.2 (Validación Funcional)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- INICIANDO PRUEBA DE REALIDAD FASE 1.2 ---"))

        # 1. Instanciar Agentes
        cap = CapitanMarketing()
        ten = TenienteMarketing()
        sar = SargentoMarketing()
        sol = SoldadoMarketing1()

        # 2. Prueba de Flujo Normal (Todo Activo por defecto)
        self.stdout.write("Escenario 1: Flujo Normal")
        try:
            cap.plan(None)
            ten.coordinar({})
            sar.ejecutar({})
            sol.realizar_tarea_manual({})
            self.stdout.write(self.style.SUCCESS("  - OK: Flujo completo exitoso."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  - FALLO: {e}"))

        # 3. Prueba de Corte: Deshabilitar Capitán
        self.stdout.write("Escenario 2: Corte por Capitán Deshabilitado")
        GovernanceKernel.alternar_estado_agente("CapitanMarketing", "DESHABILITADO")

        # El Capitán no puede planear
        try:
            cap.plan(None)
            self.stdout.write(self.style.ERROR("  - ERROR: El Capitán permitió planificar estando deshabilitado."))
        except PermissionError as e:
            self.stdout.write(self.style.SUCCESS(f"  - OK: Capitán bloqueado correctamente: {e}"))

        # El Teniente no puede coordinar (Superior Inactivo)
        try:
            ten.coordinar({})
            self.stdout.write(self.style.ERROR("  - ERROR: El Teniente permitió coordinar con superior deshabilitado."))
        except PermissionError as e:
            self.stdout.write(self.style.SUCCESS(f"  - OK: Teniente bloqueado por jerarquía: {e}"))

        # 4. Prueba de Corte: Deshabilitar Teniente
        self.stdout.write("Escenario 3: Corte por Teniente Deshabilitado")
        GovernanceKernel.alternar_estado_agente("CapitanMarketing", "ACTIVO") # Restaurar cap
        GovernanceKernel.alternar_estado_agente("TenienteMarketing", "DESHABILITADO")

        try:
            sar.ejecutar({})
            self.stdout.write(self.style.ERROR("  - ERROR: El Sargento permitió ejecutar con superior deshabilitado."))
        except PermissionError as e:
            self.stdout.write(self.style.SUCCESS(f"  - OK: Sargento bloqueado por jerarquía: {e}"))

        # 5. Restauración Total
        self.stdout.write("Escenario 4: Restauración de Cadena")
        GovernanceKernel.alternar_estado_agente("TenienteMarketing", "ACTIVO")
        try:
            sol.realizar_tarea_manual({})
            self.stdout.write(self.style.SUCCESS("  - OK: Cadena restaurada y funcional."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  - FALLO: {e}"))

        self.stdout.write(self.style.SUCCESS("--- PRUEBA DE REALIDAD FINALIZADA ---"))
