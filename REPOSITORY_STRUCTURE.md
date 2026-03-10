# REPOSITORY STRUCTURE: SARITA PLATFORM v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Date:** March 2026

```text
SARITA/
├── agents/                 # AI Prompts and Skills (LangGraph)
│   └── skills/             # Modular skill definitions
├── apps/
│   ├── desktop/            # Desktop Application (Electron + Vite + React)
│   │   ├── main/           # Main process logic
│   │   ├── preload/        # Secure bridge
│   │   └── renderer/       # UI (React)
│   └── mobile/             # Mobile Application (Expo SDK 52)
│       ├── src/            # Screens, navigation, contexts
│       └── app.json        # Expo config
├── backend/                # Modular Monolith (Django 5.0 EOS)
│   ├── ai_models/          # LLM Routing and local inference logic
│   ├── api/                # REST Layer, Middlewares, Permissions
│   ├── apps/               # 60+ Business modules (ERP, Fintech, AI)
│   │   ├── core_erp/       # Tenancy, Ledger, Accounting
│   │   ├── sarita_agents/  # AI Orchestrator N1-N7
│   │   ├── wallet/         # Fintech / Digital Wallet
│   │   ├── delivery/       # Logistics / Transport
│   │   └── admin_plataforma/# Global platform management
│   ├── puerto_gaitan_turismo/ # Core project settings and config
│   ├── scripts/            # Mission automation and stress tests
│   └── manage.py           # Django CLI
├── docs/                   # Master Blueprints and Technical Documentation
├── infrastructure/         # K8s (EKS) manifests and Docker config
├── interfaz/               # Main Web Frontend (Next.js 15 + React 19)
│   ├── src/app/            # App Router (Admin, Prestador, Descubre)
│   └── components/         # Unified UI library
├── sarita-platform/        # Shared SDK (Cross-platform logic)
│   └── shared-sdk/         # Token management and API clients
├── web-ventas-frontend/    # Sales Funnel and Conversational Acquisition (Next.js)
├── Dockerfile              # Multi-stage production image
└── docker-compose.yml      # Local dev orchestration
```
