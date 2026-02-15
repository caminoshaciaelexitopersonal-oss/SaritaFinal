# stress_test_4_3_analytics.py
import os
import django
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import requests

# Configurar Django (necesario para usar los modelos si hacemos consultas directas)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from django.test import Client
from django.contrib.auth import get_user_model

def simulate_analytics_query(client, user):
    start = time.time()
    response = client.get('/api/sarita/metrics/productivity/')
    end = time.time()
    return {
        "status": response.status_code,
        "duration": end - start
    }

def run_stress_test_analytics():
    print("🚀 INICIANDO FASE 4.3.2: PRUEBA DE SATURACIÓN DEL DASHBOARD ANALÍTICO")

    User = get_user_model()
    user, _ = User.objects.get_or_create(username="admin_stress", is_superuser=True)

    client = Client()
    client.force_login(user)

    print("--- Realizando 100 consultas simultáneas al endpoint de métricas ---")

    start_total = time.time()
    durations = []
    success_count = 0

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(simulate_analytics_query, client, user) for _ in range(100)]
        for future in futures:
            res = future.result()
            if res["status"] == 200:
                success_count += 1
            durations.append(res["duration"])

    end_total = time.time()

    avg_duration = sum(durations) / len(durations)

    print(f"\n📊 RESULTADOS SUBFASE 4.3.2:")
    print(f"⏱️ Tiempo total de ráfaga: {end_total - start_total:.2f}s")
    print(f"⏱️ Tiempo promedio por consulta: {avg_duration:.4f}s")
    print(f"✅ Consultas exitosas: {success_count}/100")

    if success_count == 100 and avg_duration < 1.0:
        print("\n🏆 PRUEBA SUPERADA: Dashboard analítico estable y optimizado.")
    else:
        print("\n⚠️ ADVERTENCIA: Degradación de rendimiento en agregaciones analíticas.")

if __name__ == "__main__":
    run_stress_test_analytics()
