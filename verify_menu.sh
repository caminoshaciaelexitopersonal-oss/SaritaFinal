#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status.

echo "--- Iniciando el Proceso de Verificación del Menú ---"

# --- 1. Iniciar Servidores en Segundo Plano ---
echo "Arrancando servidor de Backend en puerto 8000..."
kill $(lsof -t -i :8000) 2>/dev/null || true
python backend/manage.py runserver 0.0.0.0:8000 > backend_server.log 2>&1 &

echo "Arrancando servidor de Frontend en puerto 3001..."
kill $(lsof -t -i :3001) 2>/dev/null || true
(cd frontend && npm run dev -- --port 3001 > ../frontend_server.log 2>&1 &)

echo "Esperando 20 segundos a que los servidores se inicien..."
sleep 20

# --- 2. Preparar la Base de Datos ---
echo "Recreando la base de datos desde cero..."
rm -f backend/db.sqlite3
python backend/manage.py migrate
echo "Base de datos migrada."

echo "Poblando la base de datos con datos de prueba..."
python backend/manage.py setup_test_data
echo "Base de datos poblada."

# --- 3. Ejecutar la Prueba de Verificación ---
echo "Esperando 10 segundos adicionales para la sincronización del frontend..."
sleep 10

echo "Ejecutando la prueba de Playwright para el menú..."
(cd frontend && npx playwright test tests/menu.spec.ts)

# --- 4. Limpieza ---
echo "Limpiando procesos en segundo plano..."
kill $(lsof -t -i :8000) 2>/dev/null || true
kill $(lsof -t -i :3001) 2>/dev/null || true

echo "--- Proceso de Verificación Completado ---"
