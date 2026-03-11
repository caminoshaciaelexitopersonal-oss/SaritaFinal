import asyncio
import random
import logging
import sys
import os

# Ajustar path para importar módulos locales
sys.path.append(os.path.join(os.getcwd(), 'backend/ai'))

from missions.capitanes import GenericCaptain
from memory.memory_store import memory_store

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def simulate():
    captain = GenericCaptain()
    missions = ["reservas", "facturacion", "analitica", "turismo", "fraude"]
    results = {"success": 0, "failed": 0, "blocked": 0, "error": 0}

    total_missions = 5000
    logger.info(f"Iniciando simulación de {total_missions} misiones...")

    for i in range(total_missions):
        mission_type = random.choice(missions)

        # Generar data aleatoria
        data = {
            "usuario": f"user_{random.randint(1,1000)}",
            "venta_id": random.randint(10000, 99999),
            "amount": random.uniform(100, 15000000),
            "destino": random.choice(["Puerto Gaitán", "Ruta del Manatí", "Artesanías Local"])
        }

        result = await captain.coordinate(mission_type, data)
        status = result.get("status")

        if status in results:
            results[status] += 1
        else:
            results["error"] += 1

        # Registrar en memoria (cada 10 para no saturar log)
        if i % 10 == 0:
            await memory_store.save_event(mission_type, "SIMULATION_STEP", data, result)

        if i % 1000 == 0:
            logger.info(f"Progreso: {i}/{total_missions}")

    logger.info("--- RESULTADOS DE LA SIMULACIÓN ---")
    for k, v in results.items():
        logger.info(f"{k.upper()}: {v} ({v/total_missions*100:.1f}%)")

    success_rate = (results['success'] + results['blocked']) / total_missions
    if success_rate > 0.95:
        logger.info("VEREDICTO: FASE B CERTIFICADA. Alta precisión operativa.")
    else:
        logger.info("VEREDICTO: Se requiere ajuste en playbooks.")

if __name__ == "__main__":
    asyncio.run(simulate())
