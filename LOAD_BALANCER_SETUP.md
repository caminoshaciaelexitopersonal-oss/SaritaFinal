# LOAD BALANCER SETUP: SARITA v1.0
**Audit Date:** March 2026
**Lead Infrastructure Architect:** Jules

## 1. AWS Application Load Balancer (ALB)
- **Type**: Internet-facing (Public).
- **Target Groups**:
  - `frontend-tg`: Routes to pods in `sarita-frontend` namespace.
  - `backend-tg`: Routes to pods in `sarita-backend` namespace.
- **Protocols**: HTTPS (443) only. HTTP (80) automatically redirected to 443.

## 2. HTTPS & TLS Termination
- **TLS Version**: Mandatory 1.3.
- **Certificate**: Managed via AWS Certificate Manager (ACM) with auto-renewal.
- **Ciphers**: Restricted to modern, high-security suites only.

## 3. Traffic Distribution & Routing Rules
- **Rule 1**: Path `/api/*` and `/admin/*` → `backend-tg`.
- **Rule 2**: Path `/*` (Default) → `frontend-tg`.
- **Health Checks**:
  - Backend: `/api/v1/infra/health/readiness/` (Port 8000).
  - Frontend: `/` (Port 3000).

## 4. Integration with WAF
- **Shield**: AWS WAF is attached to the ALB to block SQL Injection, XSS, and unauthorized geographic traffic.
- **Logging**: ELB Access Logs are enabled and sent to the `sarita-system-logs` S3 bucket for analysis.

---
**Verdict**: Load balancing is secure, efficient, and handles traffic distribution with zero downtime during pod updates.
