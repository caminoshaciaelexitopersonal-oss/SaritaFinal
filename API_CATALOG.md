# API CATALOG: SARITA PLATFORM v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Date:** March 2026

The platform exposes a comprehensive RESTful API under the `/api/v1/` namespace, with legacy support for non-versioned endpoints.

## 1. Authentication & Security
| Endpoint | Method | Purpose |
| :--- | :---: | :--- |
| `/api/auth/login/` | POST | JWT Token acquisition |
| `/api/auth/token/refresh/` | POST | JWT Token rotation |
| `/api/auth/registration/` | POST | User enrollment |
| `/api/auth/user/` | GET | Current user profile |

## 2. Business Domains (Mi Negocio)
| Endpoint Prefix | Domain | Responsibility |
| :--- | :--- | :--- |
| `/api/v1/mi-negocio/` | ERP | General business management |
| `/api/v1/mi-negocio/ventas/` | Sales | Order and invoice management |
| `/api/v1/mi-negocio/nomina/` | HR | Payroll and employee records |
| `/api/v1/mi-negocio/contabilidad/` | Finance | Chart of accounts and fiscal periods |
| `/api/v1/mi-negocio/archivistica/` | Records | Legal document custody |

## 3. Intelligence & Agents
| Endpoint | Method | Responsibility |
| :--- | :---: | :--- |
| `/api/v1/agents/sarita/directive/` | POST | Dispatch mission to General Sarita |
| `/api/v1/agents/sadi/intent/` | POST | Acquisition agent interaction |
| `/api/v1/agents/sarita/task/<id>/` | GET | Task execution status |

## 4. Fintech & Logistics
| Endpoint Prefix | Domain | Responsibility |
| :--- | :--- | :--- |
| `/api/v1/finance/wallet/` | Fintech | Wallet balance and transactions |
| `/api/v1/operations/delivery/` | Logistics | Routing and courier assignment |
| `/api/v1/finance/indicators/` | Data | Financial ratios and KPIs |

## 5. Global Governance
| Endpoint Prefix | Domain | Responsibility |
| :--- | :--- | :--- |
| `/api/v1/governance/control-tower/` | Metrics | Real-time behavior monitoring |
| `/api/v1/governance/intelligence/` | Strategy | Decision support system |
| `/api/v1/governance/plataforma/` | Admin | Global system configuration |

**Documentation:** Auto-generated OpenAPI 3.0 schema available at `/api/schema/swagger-ui/`.
**Standard:** All write operations require `X-Sarita-Nonce` validation.
