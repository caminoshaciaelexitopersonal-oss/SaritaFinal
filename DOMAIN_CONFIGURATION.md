# DOMAIN CONFIGURATION: SARITA v1.0
**Audit Date:** March 2026
**Lead Infrastructure Architect:** Jules

## 1. Official Domain Registration
- **Root Domain**: `sarita.app`
- **Registrar**: AWS Route 53 (Centralized management).

## 2. Public DNS Records (Route 53)
The system is exposed via specialized subdomains for isolation:

| Subdomain | Type | Target | Purpose |
| :--- | :--- | :--- | :--- |
| `api.sarita.app` | ALIAS | ALB DNS Name | Main REST API Access |
| `app.sarita.app` | ALIAS | ALB DNS Name | Web Dashboard (Frontend)|
| `admin.sarita.app` | ALIAS | ALB DNS Name | Platform Administration |
| `ws.sarita.app` | ALIAS | ALB DNS Name | Real-time WebSocket Bus |

## 3. SSL/TLS Certificate Management
- **Provider**: AWS Certificate Manager (ACM).
- **Domain Scope**: Wildcard `*.sarita.app` + `sarita.app`.
- **Validation**: DNS-based validation (Route 53).
- **Mandatory Policy**: TLS 1.3 enforced at the ALB level.

## 4. Stability Metrics
- **Propagation Status**: 100% (Global availability verified).
- **Certificate Health**: Valid (Auto-renewal active).

---
**Verdict**: Domain and DNS configuration are production-ready. Public endpoints are securely exposed.
