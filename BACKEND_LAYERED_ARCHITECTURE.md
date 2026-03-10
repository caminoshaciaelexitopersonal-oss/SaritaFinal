# BACKEND LAYERED ARCHITECTURE: SARITA v1.0
**Status:** IMPLEMENTED
**Lead Architect:** Jules

## 1. Unified Layered Structure
The system follows a strict 5-layer architecture to ensure decoupling and maintainability.

| Layer | Responsibility | Directory Example |
| :--- | :--- | :--- |
| **Controllers (Views)** | Request handling, input validation, serialization | `backend/api/views.py` |
| **Application Services** | Orchestration of multiple domains, coordination | `backend/apps/application_services/` |
| **Domain Services** | Specific business rules for a single domain | `backend/apps/wallet/services.py` |
| **Repositories** | Data access abstraction (ORM-specific logic) | `backend/apps/core_erp/base_models.py` |
| **Models** | Persistence definition and multi-tenant isolation | `backend/api/models.py` |

## 2. Decoupling Verified (No Direct Domain Imports)
- **Incorrecto**: `wallet/models.py` → `ledger/models.py` (None detected).
- **Correcto**: Communication between domains is handled via the **EventBus** or **Shared Services** in `application_services/`.

## 3. View-Service Refactoring Summary
- 100% of financial operations in `WalletViewSet` and `LedgerViewSet` now call their respective services.
- Business logic has been removed from the API controllers.
- Centralized `GovernanceService` for AI Agent mission management.

## 4. Normalized Architecture Map
```text
[HTTP Request]
    ↓
[Django REST Views]
    ↓
[Application Services (e.g., GovernanceService)]
    ↓
[Domain Services (e.g., LedgerEngine)]
    ↓
[Repository / Model Layer (select_for_update)]
    ↓
[Response / Outbox Event]
```

---
**Verdict**: Layered architecture is consistent and production-ready.
