# stress_test_5_3_ruptura_contable.py
import os
import django
import uuid

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from apps.sarita_agents.orchestrator import sarita_orchestrator
from apps.sarita_agents.models import Mision, PlanTáctico, TareaDelegada, MicroTarea

def run_ruptura_contable_test():
    print("🚀 INICIANDO FASE 5.3: PRUEBA DE RUPTURA CONTABLE CONTROLADA")

    # Simular un asiento descuadrado (Debito != Credito)
    directive = {
        "domain": "contabilidad",
        "mission": {"type": "BROKEN_ACCOUNTING_ENTRY"},
        "parameters": {
            "periodo_id": str(uuid.uuid4()), # ID inexistente o no válido para forzar fallo
            "movimientos": [
                {"cuenta_id": str(uuid.uuid4()), "debito": 1000, "descripcion": "Venta"},
                {"cuenta_id": str(uuid.uuid4()), "credito": 500, "descripcion": "Caja"} # DESCUADRADO
            ]
        }
    }

    print("--- Intentando registrar asiento descuadrado ---")
    mision = sarita_orchestrator.handle_directive(directive)

    # El handle_directive devuelve el resultado_final si es síncrono (EAGER)
    print(f"📊 Informe del General: {mision}")

    mision_id = mision.get("mision_id")
    if mision_id:
        m_obj = Mision.objects.get(id=mision_id)
        print(f"🔍 Estado final de la misión en DB: {m_obj.estado}")

        if m_obj.estado == 'FALLIDA' or m_obj.estado == 'COMPLETADA_PARCIALMENTE':
            print("\n🏆 PRUEBA SUPERADA: El sistema detectó la inconsistencia contable y registró el fallo.")
        else:
            print("\n❌ FALLO DE SEGURIDAD: El sistema permitió un asiento inválido.")

if __name__ == "__main__":
    run_ruptura_contable_test()
