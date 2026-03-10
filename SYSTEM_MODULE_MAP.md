# SYSTEM MODULE MAP: SARITA v1.0
**Audit Date:** March 2026
**Lead Architect:** Jules

## 1. Repository Structure Overview
```text
/backend/                 # Core API & Modular Logic (Django 5.0)
    /api/                 # System Endpoints & Unified Serializers
    /apps/                # Domain-Specific Modules (Decoupled)
        /core_erp/        # Centralized ERP Engine (Accounting, Tenancy)
        /wallet/          # Digital Assets & Financial Custody
        /sarita_agents/   # N1-N7 Hierarchical AI Infrastructure
        /comercial/       # Sales & Marketing Automation
        /delivery/        # Logistics & Distribution Engine
/interfaz/                # Web Dashboard (Next.js 15)
/web-ventas-frontend/     # Conversion Funnel (Next.js)
/apps/mobile/             # Mobile Application (Expo)
/apps/desktop/            # POS Application (Electron)
/sarita-platform/         # Shared Logic (Shared SDK)
/k8s/                     # High-Availability Orchestration (Kubernetes)
/scripts/                 # System Management & Maintenance
```

## 2. Core Modules Identification
| Module Name | Responsibility | Dependencies | Status |
| :--- | :--- | :--- | :--- |
| **Core ERP** | Accounting, Multi-tenancy, Events | `PostgreSQL`, `Redis` | COMPLETE |
| **Wallet** | Asset management, atomic payments | `Core ERP`, `SQLite` | COMPLETE |
| **Sarita Agents**| AI Orchestration (N1-N7) | `LangGraph`, `OpenAI` | COMPLETE |
| **Interop Bridge**| International connectivity | `REST`, `gRPC` | COMPLETE |

## 3. Duplication & Redundancy Detection
- **Services**: Minor duplication between `application_services` and `domain_services` in `core_erp`.
- **Models**: Duplication of `Entity` models in `api` vs `companies` (Planned for unification).
- **Helpers**: Found redundant date formatters in `common/utils.py`.

## 4. Dead/Unused Code Detection
- **Módulos**: `apps/legacy_custody` is imported but has 0 active calls in the main workflow.
- **Imports**: Found 12 unused imports in `api/views.py`.

---
**Status**: Structural mapping completed. No architectural blockers found.
