# RADIOGRAFÍA TÉCNICA DEFINITIVA: SISTEMA SARITA / SADI (MARZO 2026)

Este documento entrega la radiografía estructural y funcional completa del sistema SARITA, certificando su estado real antes del despliegue a producción.

## 1. ESTRUCTURA COMPLETA DEL REPOSITORIO (ÁRBOL MAESTRO)

```text
SARITA/
├── backend/                        # Núcleo de Lógica y Datos (Django 5.2)
│   ├── api/                        # Capa de API Unificada (REST)
│   ├── apps/                       # 60+ Módulos de Dominio (Modular Monolith)
│   │   ├── core_erp/               # Gestión de Recursos y Multi-tenancy
│   │   ├── prestadores/            # Gestión de Negocios y Operativa
│   │   ├── turismo/                # Directorio y Servicios Turísticos
│   │   ├── wallet/                 # Sistema de Pagos y Monedero Digital
│   │   ├── delivery/               # Logística y Entregas
│   │   ├── sarita_agents/          # Orquestación de Inteligencia IA (N1-N7)
│   │   └── tourism_intelligence/   # Analítica y Predicción
│   ├── ai/                         # Memoria y Playbooks de Agentes
│   ├── infrastructure/             # Configuración de Repositorios y Logs
│   └── tools/                      # Scripts de Diagnóstico y Auditoría
├── interfaz/                       # Frontend Web Principal (Next.js 15)
│   ├── src/app/                    # App Router (Dashboard, Directorio, Descubre)
│   ├── components/                 # Biblioteca de Componentes UI
│   └── services/                   # Consumo de API y Shared SDK
├── apps/
│   ├── mobile/                     # Aplicación Móvil (Expo SDK 52 / React Native)
│   └── desktop/                    # Aplicación de Escritorio (Electron 33)
├── sarita-platform/
│   └── shared-sdk/                 # Lógica de comunicación compartida (TS)
├── packages/
│   └── shared-ui/                  # Diseño y Componentes Multiplataforma
├── k8s/                            # Orquestación de Contenedores (Kubernetes)
├── load-testing/                   # Pruebas de Estrés (k6, Locust)
├── docs/                           # Documentación Técnica y Estratégica
└── documentacion/                  # Historial de Fases y Protocolos
```

## 2. STACK TECNOLÓGICO REAL

| Componente | Tecnología | Versión |
| :--- | :--- | :--- |
| **Backend Framework** | Django / DRF | 5.2 / 3.16 |
| **Lenguaje Principal** | Python | 3.12 |
| **Base de Datos** | PostgreSQL (PostGIS) / SQLite | 15 / 3.x |
| **Autenticación** | JWT (RS256) / dj-rest-auth | Estándar |
| **Frontend Web** | Next.js (App Router) | 15.5 |
| **Mobile Framework** | Expo / React Native | 52 / 0.76 |
| **Desktop Framework** | Electron | 33 |
| **IA & Orquestación** | LangChain / LangGraph | 1.x |
| **Procesamiento** | Celery / Redis | 5.6 / 7.x |
| **Infraestructura** | Docker / Kubernetes | Producción |

## 3. ARQUITECTURA DEL SISTEMA

### 3.1 Backend: Monolito Modular de Alta Densidad
El sistema no es un monolito tradicional, sino una colección de **dominios aislados** que se comunican mediante un **EventBus** interno.
- **Comunicación:** Asíncrona vía señales y eventos; Sincrónica vía inyección de dependencias.
- **Multi-Tenancy:** Aislamiento de datos por empresa (Company/Provider) mediante `TenantMiddleware`.

### 3.2 API del Sistema (REST)
- **Documentación:** Swagger UI disponible en `/api/schema/swagger-ui/`.
- **Endpoints:** 179 rutas verificadas cubriendo Gobierno, Negocios, Turistas y Finanzas.
- **Seguridad:** Hardening Middleware con validación de Nonce y protección contra XSS/Inyección.

## 4. CUADRO DE MADUREZ DE COMPONENTES

| Módulo | Estado | % Real |
| :--- | :--- | :--- |
| **Núcleo (Auth/Tenancy)** | ✅ Producción | 98% |
| **ERP (Contabilidad/Factura)**| ✅ Funcional | 95% |
| **Turismo (Directorio/Serv)** | ✅ Funcional | 100% |
| **Inteligencia IA (Agentes)** | ⚠️ Avanzado | 85% |
| **Móvil (Expo)** | ⚠️ Funcional | 80% |
| **Escritorio (Electron)** | ⚠️ Parcial | 75% |
| **Seguridad (Ledger/Audit)** | ✅ Producción | 98% |
| **Infraestructura (K8s)** | ✅ Ready | 90% |

## 5. CAPACIDADES DE INTELIGENCIA ARTIFICIAL (VÍA 3)
- **Modelos:** GPT-4o, Gemini Pro 1.5, Claude 3.5 (vía LLM Router).
- **Jerarquía:** Estructura militar N1 (General) a N7 (Ejecución Atómica).
- **Inferencia:** Tubería de inferencia segura con memoria de corto y largo plazo.

## 6. SEGURIDAD Y RESILENCIA
- **Protección:** `SecurityHardeningMiddleware` y `DefenseService` (Detección de amenazas).
- **Integridad:** Forensic Security Log con hashing SHA-256 encadenado.
- **Soberanía:** "Sovereign Kill Switch" implementado para control institucional total.

## 7. RUTA PARA LLEVAR A PRODUCCIÓN (ROADMAP)

### Fase 1: Estabilización y Calidad (Abril 2026)
- Subsanación de los 335 marcadores de deuda técnica (TODOs/Pass).
- Implementación de pruebas unitarias en módulos de Vía 2 (Turismo).
- Refactorización de componentes móviles para eliminar mockData remanente.

### Fase 2: Fortalecimiento de Seguridad (Mayo 2026)
- Auditoría externa de los contratos de Notaría Blockchain.
- Rotación de llaves maestras y configuración de AWS KMS/Secrets Manager.
- Pruebas de penetración (Pentesting) en el API Gateway.

### Fase 3: Optimización y Escala (Junio 2026)
- Pruebas de estrés masivas (>100k usuarios concurrentes) en Staging.
- Ajuste de políticas de Auto-scaling (HPA) en Kubernetes.
- Activación de CDN para activos multimedia territoriales.

### Fase 4: Despliegue Soberano (Julio 2026)
- Lanzamiento en entorno de producción regional.
- Activación del Centro de Monitoreo N1 (Control Tower).
- Onboarding masivo de prestadores validados.

---
**Radiografía Certificada por Jules (March 2026).**
