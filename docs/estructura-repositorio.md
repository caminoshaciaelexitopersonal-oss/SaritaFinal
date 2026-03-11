# Estructura del Repositorio SARITA v1.0
```text
sarita/
├── backend/                # Núcleo Django 5.0 (Cerebro Central)
│   ├── apps/               # 60+ Módulos de negocio (ERP, Fintech, AI)
│   ├── api/                # Capa REST v1 y Auth
│   └── application/        # Servicios de Aplicación (DDD)
├── interfaz/               # Frontend Web Next.js 15 (Portal Administrativo)
├── apps/
│   ├── mobile/             # Aplicación Expo (Gestión en Campo)
│   └── desktop/            # Aplicación Electron (Terminal POS)
├── packages/
│   └── shared-ui/          # Librería de Componentes Unificada
├── sarita-platform/
│   └── shared-sdk/         # Lógica de Negocio y API Client compartido
├── k8s/                    # Manifiestos de Orquestación y Monitoreo
└── docs/                   # Documentación Maestra del Ecosistema
```
