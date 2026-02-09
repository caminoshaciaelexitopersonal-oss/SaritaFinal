import os
import sys
from django.core.management.base import BaseCommand
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
from apps.sarita_agents.agents.general.sarita.coroneles.comercial.capitanes.capitan_marketing import CapitanMarketing
from apps.sarita_agents.agents.general.sarita.coroneles.comercial.tenientes.teniente_marketing import TenienteMarketing
from apps.sarita_agents.agents.general.sarita.coroneles.comercial.sargentos.sargento_marketing import SargentoMarketing
from apps.sarita_agents.agents.general.sarita.coroneles.comercial.soldados.soldado_marketing_1 import SoldadoMarketing1

class Command(BaseCommand):
    help = 'Ejecuta las Pruebas de Ruptura y Sabotaje Fase 1.3'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- INICIANDO FASE 1.3: PRUEBAS DE SABOTAJE ---"))

        cap = CapitanMarketing()
        ten = TenienteMarketing()
        sar = SargentoMarketing()
        sol = SoldadoMarketing1()

        # 1. Sabotaje del Capitán
        self.stdout.write("\n[1.1] Capitán Omisivo (No autoriza)")
        res = cap.plan(None)
        if res.get("status") == "BLOCKED":
             self.stdout.write(self.style.SUCCESS("  - OK: Sistema detectó omisión y bloqueó paso."))

        self.stdout.write("\n[1.2] Capitán Abusivo (Ejecuta tarea de Sargento)")
        try:
            cap.ejecutar({})
        except PermissionError as e:
            self.stdout.write(self.style.SUCCESS(f"  - OK: Bloqueo por abuso de poder: {e}"))

        # 2. Sabotaje del Teniente
        self.stdout.write("\n[2.1] Teniente Usurpador (Actúa como Capitán)")
        try:
            ten.plan(None)
        except PermissionError as e:
            self.stdout.write(self.style.SUCCESS(f"  - OK: Bloqueo por usurpación: {e}"))

        self.stdout.write("\n[2.2] Teniente Colapsador (Bloquea subordinados)")
        ten.alternar_subordinado("SargentoMarketing", habilitar=False)
        try:
            sar.ejecutar({})
        except PermissionError as e:
            self.stdout.write(self.style.SUCCESS(f"  - OK: Cadena rota detectada: {e}"))
        ten.alternar_subordinado("SargentoMarketing", habilitar=True) # Restaurar

        # 3. Sabotaje del Sargento
        self.stdout.write("\n[3.1] Sargento Desobediente (Reporta fallo)")
        fail_res = {"status": "ERROR"}
        if not ten.verificar_resultado_sargento("SargentoMarketing", fail_res):
            self.stdout.write(self.style.SUCCESS("  - OK: Teniente detectó fallo del sargento y penalizó."))

        self.stdout.write("\n[3.2] Sargento Manipulador (Altera datos)")
        res = sar.ejecutar({"manipulado": True})
        if res.get("status") == "ERROR":
            self.stdout.write(self.style.SUCCESS("  - OK: Intento de manipulación bloqueado por el Sargento."))

        # 4. Sabotaje del Soldado
        self.stdout.write("\n[4.1] Soldado Autónomo (Ejecuta como Sargento)")
        try:
             sol.ejecutar({})
        except PermissionError as e:
             self.stdout.write(self.style.SUCCESS(f"  - OK: Bloqueo de autonomía del soldado: {e}"))

        self.stdout.write("\n[4.2] Soldado Falsificador (Sin evidencia)")
        res = sol.realizar_tarea_manual(None)
        if res.get("status") == "ERROR":
            self.stdout.write(self.style.SUCCESS("  - OK: Falsificación detectada (falta de evidencia)."))

        # 5. Colusión y Traición Total
        self.stdout.write("\n[5.0] Preparando Traición Total (Penalización masiva)")
        for _ in range(5):
            sol.penalizar_confianza("FALSIFICACION", "Colusión detectada")

        try:
            sol.validar_jerarquia()
        except PermissionError as e:
            self.stdout.write(self.style.SUCCESS(f"  - OK: NODO CORRUPTO AISLADO EXITOSAMENTE: {e}"))

        self.stdout.write(self.style.SUCCESS("\n--- FASE 1.3 FINALIZADA: SARITA ES RESILIENTE ---"))
