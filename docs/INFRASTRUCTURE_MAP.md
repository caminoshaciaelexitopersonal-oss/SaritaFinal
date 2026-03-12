# INFRASTRUCTURE MAP: SARITA PLATFORM v1.0
**Lead Auditor:** Jules (Senior AI Software Engineer)
**Date:** March 2026

The platform is designed for high-availability cloud deployment using container orchestration.

## 1. Container Architecture (Docker)
| Service | Image / Base | Role |
| :--- | :--- | :--- |
| `backend` | Python 3.11-slim | Core Django application (Gunicorn) |
| `frontend` | Node.js 20 | Next.js 15 SSR and static assets |
| `celery-worker` | Python 3.11-slim | Async task execution and AI missions |
| `db` | PostgreSQL 15 | Primary relational data persistence |
| `redis` | Redis 7 | Message broker and caching layer |

## 2. Orchestration (Kubernetes / EKS)
| Resource | Purpose |
| :--- | :--- |
| `deployment.yaml` | Multi-replica management for Backend and Workers |
| `hpa.yaml` | Horizontal Pod Autoscaling (CPU > 70%) |
| `service.yaml` | Internal routing and Load Balancer exposure |

## 3. Data Storage & Networking
- **PostgreSQL 15:** Multi-tenant schemas and isolated domain databases.
- **Amazon S3:** Custody of static assets and legal documents.
- **Cloudflare / AWS WAF:** Perimeter security and CDN.

**Maturity Status:** 100% Infrastructure-as-Code (IaC) readiness for AWS EKS.
