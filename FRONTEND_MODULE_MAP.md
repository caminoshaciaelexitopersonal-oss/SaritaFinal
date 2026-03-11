# FRONTEND MODULE MAP: SARITA PLATFORM v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Date:** March 2026

The SARITA Web Frontend is built with Next.js 15 using the App Router architecture.

| Module / Route | User Profile | Purpose |
| :--- | :--- | :--- |
| `src/app/dashboard/admin` | Gobierno / Admin | Institutional management and territorial analytics |
| `src/app/dashboard/prestador` | Prestador | "Mi Negocio" operational dashboard |
| `src/app/descubre` | Ciudadano / Turista | Public portal for destination discovery |
| `src/app/dashboard/admin-plataforma` | SuperAdmin | Global platform settings and AI orchestration |
| `src/app/mi-viaje` | Turista | Personalized traveler itinerary and wallet |
| `src/app/directorio` | Public | Marketplace of providers and artisans |
| `src/app/dashboard/login` | All | Unified authentication gateway |
| `src/app/checkout` | Turista | Payment and service booking flow |
| `src/app/mofu` | Prospect | Middle-of-the-funnel acquisition interface |

**Architecture:** Next.js 15 + React 19 + Tailwind CSS 4.
**Integration:** Consumes the centralized Django API via `httpClient` (Shared SDK).
**Duplication Note:** Strategic duplication exists with `web-ventas-frontend` for conversational marketing independence.
