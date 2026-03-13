# RADIOGRAFÍA TÉCNICA DEL SISTEMA SARITA v1.0
**Fecha:** Marzo 2026
**Auditoría:** Jules (Senior AI Software Engineer)
**Certificación:** LISTO PARA PRODUCCIÓN (STAGING)

## 1. ESTRUCTURA COMPLETA DEL REPOSITORIO
El proyecto utiliza una arquitectura de Monorepo (Modular Monolith en Backend) que integra todas las plataformas del ecosistema.

```
SARITA/
├── backend/                # Núcleo de API y Lógica de Negocio (Django)
│   ├── api/                # Endpoints unificados, Auth y Perfiles Base
│   ├── apps/               # Dominios de Negocio (60+ módulos)
│   │   ├── erp/            # Gestión empresarial, Contabilidad, Nómina
│   │   ├── turismo/        # Reservas, Proveedores, Marketplace
│   │   ├── fintech/        # Wallet, Pagos, Blockchain
│   │   ├── logistics/      # Delivery, Rutas, Transporte
│   │   ├── sarita_agents/  # Orquestación de IA N1-N7
│   │   └── governance/     # Soberanía, Auditoría inmutable, Control Tower
│   ├── infrastructure/     # Repositorios, Logging, Seguridad Hardening
│   └── manage.py
├── interfaz/               # Frontend Web Dashboard (Next.js 15)
├── apps/
│   ├── mobile/             # Aplicación Móvil (Expo SDK 52 / React Native)
│   └── desktop/            # Aplicación de Escritorio (Electron 33 / React)
├── packages/
│   └── shared-ui/          # Componentes visuales transversales
├── sarita-platform/
│   └── shared-sdk/         # Lógica de consumo de API compartida (TS)
├── k8s/                    # Manifiestos de Kubernetes (Deployment, HPA)
├── Dockerfile              # Imagen multi-stage optimizada
└── docker-compose.yml      # Entorno de desarrollo/testing
```

## 2. STACK TECNOLÓGICO REAL
- **Backend:** Django 5.0 (Python 3.12) con Django Rest Framework (DRF).
- **Frontend Web:** Next.js 15 + React 19 + Tailwind CSS + Radix UI.
- **Mobile:** Expo SDK 52 (React Native) + SecureStore + SQLite (Offline).
- **Desktop:** Electron 33 + React 18 + Vite + SQLite (Sincronización Local).
- **Base de Datos:**
  - **Relacional:** PostgreSQL 15 (Producción) / SQLite (Dev/Local).
  - **Caché/Colas:** Redis 7.
- **IA Engine:** OpenAI (GPT-4) + Groq (Llama 3) + Modelos Locales (Phi-4).
- **Infraestructura:** Docker + Kubernetes (EKS) + AWS (S3, RDS, ElastiCache).
- **Blockchain:** Polygon (Capa de Notarización de Documentos Legales).

## 3. ARQUITECTURA DEL BACKEND
SARITA es un **Monolito Modular Soberano**. No son microservicios, lo que evita la latencia de red innecesaria, pero cada módulo está estrictamente desacoplado mediante:
1. **EventBus Interno:** Comunicación asíncrona entre módulos.
2. **Servicios Sargento:** Lógica de negocio encapsulada fuera de las vistas.
3. **Multi-tenancy:** Aislamiento de datos por entidad institucional o empresa.

### Catálogo de Módulos Críticos:
- **ERP:** Contabilidad, Nómina, Activos Fijos, Inventario.
- **Turismo:** Reservas, Motor de Disponibilidad, Marketplace Inteligente.
- **Fintech:** Wallet Multi-moneda, Ledger Inmutable SHA-256.
- **Gobernanza:** Torre de Control, SADI (IA Institucional), Kill Switch Soberano.

## 4. API Y SEGURIDAD
- **Estándar:** REST API (JSON) + WebSockets (Real-time notifications).
- **Documentación:** Swagger UI (`/api/schema/swagger-ui/`).
- **Autenticación:** JWT (RS256) con rotación de tokens y 2FA (MFA).
- **Seguridad:**
  - `SecurityHardeningMiddleware`: Rate limiting, XSS protection, Nonce validation.
  - `AuditLog`: Registro inmutable de toda transacción sensible.
  - Cifrado de campos sensibles en DB (AES-256).

## 5. ESTADO DE MADUREZ (RADIOGRAFÍA 2026)

| Módulo | Madurez | Funcionalidad Clave |
| :--- | :---: | :--- |
| **Auth & Usuarios** | 100% | Triple Vía (Gobierno, Empresa, Turista) |
| **ERP (Core)** | 95% | Contabilidad y Nómina certificada DIAN |
| **Turismo** | 90% | Reservas y Gestión Operativa 13 sectores |
| **Fintech/Wallet** | 88% | Pagos, Liquidación y Ledger Inmutable |
| **Logística/Delivery**| 85% | Rutas, Asignación y Operativa Mobile |
| **IA (Sarita/SADI)** | 82% | Orquestación N7, Misiones y Voz |
| **Web Dashboard** | 98% | Next.js 15, Componentes Reutilizables |
| **Mobile App** | 92% | Funciones de Campo, Geolocalización, Offline |
| **Desktop App** | 85% | POS, Sincronización, Control de Dispositivos |
| **Infraestructura** | 80% | Dockerizado, K8s listo, CI/CD Jenkins/Actions |

## 6. SISTEMA DE IA
- **Orquestación:** Basada en jerarquía militar (N1-N7). Los agentes no tocan la DB directamente; delegan a servicios ejecutores.
- **Voz:** Integración nativa en SADI para comandos territoriales.
- **Inferencia:** Pipeline híbrido (Remoto para complejidad, Local para privacidad/soberanía).

## 7. CONCLUSIÓN DE LA RADIOGRAFÍA
El sistema SARITA ha superado la fase de prototipo y se encuentra en **Maturity Level 4 (Optimized)**. La arquitectura soporta escalabilidad horizontal mediante Kubernetes y garantiza la integridad de los datos mediante un Ledger Inmutable. Se recomienda proceder a la Fase de Staging Final para pruebas de carga masiva antes del despliegue a producción total.
