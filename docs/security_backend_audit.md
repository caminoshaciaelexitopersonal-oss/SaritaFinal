# Auditoría de Seguridad y Observabilidad del Backend - SARITA v1.0

## 1. Validación de Identidad (JWT RS256)

El sistema utiliza firma asimétrica para la generación de tokens de acceso, garantizando la máxima seguridad en la comunicación cliente-servidor.

*   **Algoritmo**: RS256 (RSA Signature with SHA-256).
*   **Claves**: Almacenadas en `backend/keys/` (jwt-private.pem y jwt-public.pem).
*   **Rotación**: Configurada vía SimpleJWT con `ROTATE_REFRESH_TOKENS: True`.
*   **Seguridad de Cookies**: `JWT_AUTH_HTTPONLY: True` para mitigar ataques XSS.

**Estado**: Certificado.

## 2. Blindaje de Aplicación (Hardening)

Se ha verificado el funcionamiento del `SecurityHardeningMiddleware`:

*   **Rate Limiting por Rol**:
    *   `TURISTA`: 150 req/min.
    *   `PRESTADOR`: 500 req/min.
    *   `SUPERADMIN`: 1000 req/min.
*   **Protección contra Replay Attacks**: Implementada mediante validación de Nonce (`X-Sarita-Nonce`) en métodos mutables (POST, PUT, DELETE).
*   **Security Headers**: Activación de HSTS, X-Frame-Options (DENY) y X-Content-Type-Options.

**Estado**: Certificado.

## 3. Observabilidad y Métricas

El sistema implementa logging estructurado para auditoría forense:

*   **Formato**: JSON (vía `EnterpriseJSONFormatter`).
*   **Trazabilidad**: Uso de `correlation_id` para vincular eventos a través de múltiples servicios.
*   **Alertas**: Configuración de alertas automáticas para rupturas de integridad en el ledger y tasas de error > 5%.

**Estado**: Operativo.

---
**Resultado de la Auditoría**: El backend de SARITA presenta una postura de seguridad robusta, cumpliendo con los estándares de la industria para aplicaciones financieras y gubernamentales.
