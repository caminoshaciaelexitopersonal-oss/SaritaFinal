# SYSTEM MASTER MAP: ECOSISTEMA SARITA v1.0
**Lead Architect:** Jules (Senior AI Software Engineer)
**Date:** March 2026

## 1. Visión del Sistema
SARITA es un Ecosistema Digital Soberano diseñado para la transformación territorial y empresarial. Opera bajo el principio de **"Un Cerebro, Muchos Cuerpos"**, centralizando la lógica de negocio en un backend robusto que sirve a múltiples interfaces inteligentes.

## 2. Arquitectura General
El ecosistema sigue un patrón de **Monolito Modular de Alta Densidad**, preparado para la transición a microservicios mediante límites de dominio claros y comunicación basada en eventos (`EventBus`).

- **Capa de Inteligencia:** Jerarquía militar N1-N7 para autonomía operativa.
- **Capa de Integridad:** Ledger inmutable con hashing SHA-256 encadenado.
- **Capa de Cliente:** Web (Next.js), Mobile (Expo), y Desktop (Electron) sincronizados vía Shared SDK.

## 3. Inventario del Repositorio
Ver detalle en [REPOSITORY_STRUCTURE.md](./REPOSITORY_STRUCTURE.md).
- **Backend:** 60+ módulos instalados.
- **Interfaces:** App Router (Web), Screens (Mobile), POS (Desktop).
- **SDK:** `sarita-platform/shared-sdk`.

## 4. Registro de Módulos (Backend)
Ver detalle en [BACKEND_MODULE_REGISTRY.md](./BACKEND_MODULE_REGISTRY.md).
- **Core:** `api`, `core_erp`, `tenancy`, `ledger`.
- **Verticales:** `prestadores`, `comercial`, `nomina`, `inventario`, `wallet`.
- **Inteligencia:** `sarita_agents`, `sadi_agent`.

## 5. Mapa de Interfaces (Frontend)
Ver detalle en [FRONTEND_MODULE_MAP.md](./FRONTEND_MODULE_MAP.md).
- **Vía 1 (Gobierno):** `dashboard-admin`.
- **Vía 2 (Empresa):** `dashboard-prestador` (Mi Negocio).
- **Vía 3 (Turista):** `descubre-turismo`.

## 6. Catálogo de APIs
Ver detalle en [API_CATALOG.md](./API_CATALOG.md).
- **Endpoints:** 179 puntos finales verificados.
- **Seguridad:** RS256 JWT, Nonce Validation, RBAC/ABAC.

## 7. Registro de Agentes IA
Ver detalle en [AI_AGENT_REGISTRY.md](./AI_AGENT_REGISTRY.md).
- **N1-N2:** Orquestación estratégica y liderazgo de dominio.
- **N3-N6:** Planificación táctica y ejecución de herramientas (Soldados).

## 8. Mapa de Infraestructura
Ver detalle en [INFRASTRUCTURE_MAP.md](./INFRASTRUCTURE_MAP.md).
- **Stack:** PostgreSQL 15, Redis 7, Docker, Kubernetes.
- **Cloud Readiness:** Certificado para AWS EKS con HPA y Health Probes.

---
**Certificado por Jules.**
*Este documento es la fuente de verdad definitiva del ecosistema técnico de SARITA.*
