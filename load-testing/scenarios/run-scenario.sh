#!/bin/bash

# SARITA LOAD TESTING RUNNER (FASE 9)
# Uso: ./run-scenario.sh [10k|100k|1M]

SCENARIO=$1
HOST="http://localhost:8000"

case $SCENARIO in
  "10k")
    echo "--- Iniciando Escenario 1: 10,000 Usuarios ---"
    locust -f load-testing/locust-tests/locustfile.py --headless -u 10000 -r 100 --run-time 30m --host $HOST --csv load-testing/reports/test_10k_users
    ;;
  "100k")
    echo "--- Iniciando Escenario 2: 100,000 Usuarios ---"
    locust -f load-testing/locust-tests/locustfile.py --headless -u 100000 -r 500 --run-time 1h --host $HOST --csv load-testing/reports/test_100k_users
    ;;
  "1M")
    echo "--- Iniciando Escenario 3: 1,000,000 Usuarios (STRESS MAX) ---"
    # Para 1M se recomienda k6 distribuido o Locust en modo Master/Slave
    k6 run --vus 100000 --duration 2h load-testing/k6-tests/test-flow.js --summary-export load-testing/reports/test_1M_users_summary.json
    ;;
  *)
    echo "Por favor especifica un escenario válido: 10k, 100k, 1M"
    ;;
esac
