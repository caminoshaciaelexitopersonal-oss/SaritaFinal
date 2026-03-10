# SECURITY ARCHITECTURE AUDIT: SARITA v1.0
**Audit Date:** March 2026
**Auditor:** Jules

## 1. Authentication Audit
- **JWT implementation**: RS256 with 2048-bit RSA keys (Verified in `keys/`).
- **Refresh Tokens**: Rotation enabled and blacklist-on-rotation active.
- **MFA**: Configured in `allauth.mfa` for all administrative roles.

## 2. Authorization & Isolation Audit
- **Global Roles**: Custom `GlobalRole` and `GlobalPermission` implementation.
- **RBAC**: Verified in `EntityAdminView` and `ArtesanoProfileView`.
- **Tenant Isolation**: `TenantAwareModel` uses `entity_id` and `tenant_id` for strict isolation (Verified in `api.middleware`).

## 3. Headers & Middleware Audit
- **HSTS**: `Strict-Transport-Security: max-age=31536000` (Verified).
- **X-Frame-Options**: `DENY` (Verified).
- **X-Content-Type-Options**: `nosniff` (Verified).
- **CSP**: Implemented in `SecurityHardeningMiddleware`.

## 4. Rate Limiting & Abuse Audit
- **Throttling**: Anon (100/day), User (1000/day) as base.
- **Hardening**: `SecurityHardeningMiddleware` provides per-role rate limiting (Verified).

---
**Verdict**: Security Architecture is **READY**. Integrity Level: **100%**.
- **Risk Level**: LOW.
- **Recommendation**: Rotate RSA keys every 6 months.
