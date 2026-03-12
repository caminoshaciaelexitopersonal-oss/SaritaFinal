# Reporte de Seguridad Backend en Producción - SARITA v1.0

## 1. Seguridad a Nivel de Aplicación (Backend)

### 1.1 Sanitización y Validación de Entradas
*   **Validación de Esquema**: Se utiliza **Django REST Framework (DRF) Serializers** para forzar tipos de datos y longitudes máximas en cada entrada.
*   **XSS & SQL Injection**: El ORM de Django y los motores de plantillas de DRF escapan automáticamente las salidas y utilizan consultas parametrizadas.
*   **Sanitización Adicional**: Se ha implementado el uso de librerías de limpieza para campos de texto enriquecido (Markdown) para prevenir inyecciones de scripts.

### 1.2 Protección de Sesión (JWT RS256)
*   **Firma Asimétrica**: Los tokens son firmados con una clave privada RSA de 2048 bits y validados con una pública, impidiendo la falsificación de identidad incluso si el servidor de validación se ve comprometido.
*   **Rotación de Tokens**: Implementación de **Refresh Tokens** con rotación obligatoria para minimizar la vida útil de los tokens de acceso comprometidos.
*   **HttpOnly & Secure Cookies**: Los tokens se transmiten bajo banderas de seguridad del navegador para evitar el robo vía JavaScript.

### 1.3 Blindaje Dinámico (Rate Limiting)
*   **Control por Rol**: Implementado vía `SecurityHardeningMiddleware`.
    *   `TURISTA`: 150 req/min.
    *   `PRESTADOR`: 500 req/min.
    *   `SUPERADMIN`: 1000 req/min.
*   **Protección Anti-Replay**: Validación obligatoria de **Nonce** en cabecera `X-Sarita-Nonce` para todas las operaciones de escritura (POST, PUT, DELETE).

## 2. Seguridad de Infraestructura

### 2.1 Firewall y Acceso de Red
*   **SSH Hardening**: Acceso restringido únicamente a IPs de la VPN administrativa. Autenticación exclusiva por llave pública.
*   **Seguridad de Puertos**: Solo los puertos 80/443 (HTTP/S) están expuestos al balanceador de carga. Todos los demás servicios (DB, Redis) operan en subredes privadas aisladas.
*   **Mitigación DDoS**: Protección nativa a través de Cloudflare WAF para filtrado de ataques de capa 7.

### 2.2 Protección contra Fuerza Bruta
*   **Bloqueo de IP**: Integración con Redis para bloquear temporalmente IPs que excedan los umbrales de fallos de autenticación (5 intentos fallidos = 30 min de bloqueo).

---
**Resultado**: El sistema cumple con los requisitos de seguridad empresarial para el manejo de datos financieros y ciudadanos.
