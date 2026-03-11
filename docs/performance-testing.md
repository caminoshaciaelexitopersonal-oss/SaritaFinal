# SISTEMA DE PRUEBAS DE CARGA Y ALTO RENDIMIENTO (FASE 9)
**Lead Performance Engineer:** Jules (Senior AI Software Engineer)
**Date:** March 2026

## 1. Estrategia de Simulación Masiva
Para asegurar la estabilidad de SARITA v1.0 a escala nacional, se ha implementado un laboratorio de pruebas de carga que simula hasta **1,000,000 de usuarios concurrentes**.

### Herramientas
- **Locust (Python):** Simulación de comportamientos complejos de usuarios (Turistas, Prestadores, Admins).
- **k6 (JavaScript/Go):** Pruebas de flujo funcional de alta densidad y baja latencia.

## 2. Escenarios de Prueba
| Escenario | Usuarios | Objetivo | Herramienta |
| :--- | :--- | :--- | :--- |
| **Escenario 1** | 10,000 | Estabilidad inicial y latencia base. | Locust |
| **Escenario 2** | 100,000 | Identificación de cuellos de botella en DB. | Locust |
| **Escenario 3** | 1,000,000 | Validación de escala nacional (Stress Test). | k6 |

## 3. Métricas Clave de Rendimiento (KPIs)
- **Response Time (p95):** < 500ms para endpoints críticos.
- **Error Rate:** < 1% bajo carga sostenida.
- **CPU/Memory Saturation:** Monitoreo de nodos de aplicación y base de datos.
- **Transaction Integrity:** Verificación de no-duplicidad en reservas concurrentes.

## 4. Estructura del Laboratorio
```text
load-testing/
├── locust-tests/   # Scripts de comportamiento (Python)
├── k6-tests/       # Pruebas de flujo (JS)
├── scenarios/      # Scripts de ejecución automatizada
└── reports/        # Resultados de ejecución (CSV/JSON/HTML)
```

## 5. Próximos Pasos
- Integración de los reportes de rendimiento al Pipeline de CI/CD.
- Optimización de los cuellos de botella detectados en el Escenario 3.
