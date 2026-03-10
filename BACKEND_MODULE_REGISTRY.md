# BACKEND MODULE REGISTRY: SARITA PLATFORM v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Date:** March 2026

The SARITA backend is a High-Density Modular Monolith built on Django 5.0.

| Module Name | Purpose / Responsibility | Domain |
| :--- | :--- | :--- |
| `api` | Core REST API, Authentication, and User Management | Global |
| `core_erp` | Immutable Ledger, Multi-tenancy, and Accounting Core | ERP Core |
| `sarita_agents` | AI Orchestration Hierarchy (N1-N7) | Intelligence |
| `sadi_agent` | Conversational Marketing and Acquisition Agent | Marketing |
| `wallet` | Digital Wallet, Payments, and Escrow | Fintech |
| `delivery` | Logistics, Routing, and Courier Management | Operations |
| `prestadores` | Provider Business Logic ("Mi Negocio") | ERP Domain |
| `gestion_comercial`| CRM, Sales Funnels, and Marketing Content | Sales |
| `gestion_financiera`| Treasury, Budgeting, and Financial Ratios | Finance |
| `nomina` | Payroll Liquidation and Human Capital | HR |
| `inventario` | Warehouse and Product Stock Management | ERP Domain |
| `admin_plataforma` | Global Governance and Platform Settings | Admin |
| `tokenization` | Asset Tokenization and Capital Units | Fintech |
| `governance_live` | Systemic State Monitoring and Memory | Governance |
| `peace_net` | Global Stability and Risk Mitigation | Resilience |
| `audit` | Forensic Logging and Security Auditing | Security |
| `operational_intelligence` | SaaS Metrics and Revenue Forecasting | Data |
| `sovereign_infrastructure` | Regulatory Profiles and Jurisdictional Nodes | Infrastructure |

**Total Verified Business Modules:** 60+
**Architectural Pattern:** Domain-Driven Modular Monolith with EventBus decoupling.
