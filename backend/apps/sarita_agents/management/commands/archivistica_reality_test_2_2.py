from django.core.management.base import BaseCommand
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
from apps.sarita_agents.agents.archivistica.capitanes.capitancustodiaalmacenamiento import CapitanCustodiaAlmacenamiento
from apps.sarita_agents.agents.archivistica.tenientes.tenientecifradoarchivos import TenienteCifradoArchivos
from apps.sarita_agents.agents.archivistica.sargentos.sargentocifradoaes import SargentoCifradoAES
from apps.sarita_agents.agents.archivistica.soldados.soldadocifradoaes_1 import SoldadoCifradoAES_1

class Command(BaseCommand):
    help = 'Prueba de Realidad FASE 2.2 — Validación Funcional Archivística'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- INICIANDO PRUEBA DE REALIDAD ARCHIVÍSTICA 2.2 ---"))

        # 1. Registro Manual (para asegurar persistencia en la ejecución del comando)
        self._register_test_agents()

        # 2. Instanciar Cadena de Mando
        cap = CapitanCustodiaAlmacenamiento()
        ten = TenienteCifradoArchivos()
        sar = SargentoCifradoAES()
        sol = SoldadoCifradoAES_1()

        # ESCENARIO 1: Flujo Normal (Todo Activo)
        self.stdout.write("\nEscenario 1: Flujo Normal de Mando")
        try:
            res_cap = cap.handle_order({})
            res_ten = ten.handle_tactics({})
            res_sar = sar.handle_operation({})
            res_sol = sol.execute_task({})
            self.stdout.write(self.style.SUCCESS(f"  - ÉXITO: Flujo archivístico completado: {res_sol['status']}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  - FALLO INESPERADO: {e}"))

        # ESCENARIO 2: Jerarquía Rota (Superior Inactivo)
        self.stdout.write("\nEscenario 2: Cadena Rota (Capitán Deshabilitado)")
        GovernanceKernel.alternar_estado_agente("CapitanCustodiaAlmacenamiento", "DESHABILITADO")
        try:
            ten.handle_tactics({})
            self.stdout.write(self.style.ERROR("  - ERROR: Teniente permitió acción con superior inactivo."))
        except PermissionError as e:
            self.stdout.write(self.style.SUCCESS(f"  - ÉXITO: Bloqueo jerárquico activo: {e}"))

        # Restaurar
        GovernanceKernel.alternar_estado_agente("CapitanCustodiaAlmacenamiento", "ACTIVO")

        # ESCENARIO 3: Usurpación de Nivel
        self.stdout.write("\nEscenario 3: Intento de Usurpación (Soldado intentando orquestar)")
        try:
            sol.validar_jerarquia(nivel_requerido="CAPITAN")
            self.stdout.write(self.style.ERROR("  - ERROR: El Soldado usurpó nivel de mando."))
        except PermissionError as e:
            self.stdout.write(self.style.SUCCESS(f"  - ÉXITO: Usurpación bloqueada: {e}"))

        # ESCENARIO 4: Ejecución sin Subordinados (Falla Estructural)
        self.stdout.write("\nEscenario 4: Falla por fuerza incompleta (regla de 5)")
        original_get_soldados = sar._get_soldados
        sar._get_soldados = lambda: ["Soldado1"] # Solo 1
        try:
            sar.handle_operation({})
            self.stdout.write(self.style.ERROR("  - ERROR: Sargento permitió ejecución con fuerza incompleta."))
        except ValueError as e:
            self.stdout.write(self.style.SUCCESS(f"  - ÉXITO: Bloqueo estructural activo: {e}"))
        sar._get_soldados = original_get_soldados

        self.stdout.write(self.style.SUCCESS("\n--- PRUEBA FINALIZADA ---"))

    def _register_test_agents(self):
        agents = {
            "CapitanCustodiaAlmacenamiento": {"nivel": "CAPITAN", "superior": "CoronelArchivisticoGeneral"},
            "TenienteCifradoArchivos": {"nivel": "TENIENTE", "superior": "CapitanCustodiaAlmacenamiento"},
            "SargentoCifradoAES": {"nivel": "SARGENTO", "superior": "TenienteCifradoArchivos"},
            "SoldadoCifradoAES_1": {"nivel": "SOLDADO", "superior": "SargentoCifradoAES"}
        }
        for name, meta in agents.items():
            GovernanceKernel.register_agent(name, {
                **meta,
                "dominio": "GESTION_ARCHIVISTICA",
                "mision": "Test",
                "estado": "ACTIVO"
            })
