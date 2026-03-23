# Modelo de Seguridad y Blindaje - Sistema SARITA

## 1. Autenticación y Autorización
SARITA implementa un modelo de seguridad de "Cero Confianza" (Zero Trust).

### 1.1 Autenticación Fuerte
- **Multi-Factor Authentication (MFA):** Requerido para todos los roles administrativos.
- **JWT (JSON Web Tokens):** Utilizados para la comunicación entre el frontend y el backend, con tiempos de expiración cortos y rotación de tokens.
- **Identidad Federada:** Soporte para OAuth2 y OpenID Connect para usuarios turísticos.

### 1.2 Autorización por Roles (RBAC)
Los permisos se gestionan mediante una jerarquía de roles clara:
- **SUPER_ADMIN:** Control total del sistema.
- **PROVIDER_ADMIN:** Gestión de un negocio específico.
- **OPERATOR:** Acceso a funciones operativas (Ventas, Check-in).
- **TOURIST:** Acceso a servicios de consumo.

## 2. Protección de Datos

### 2.1 Cifrado
- **En Tránsito:** Obligatorio uso de TLS 1.3 para todas las comunicaciones (HTTPS, WSS).
- **En Reposo:** Cifrado de bases de datos mediante AES-256. Los campos sensibles (ej. documentos de identidad, teléfonos) se cifran a nivel de aplicación.

### 2.2 Registro Inmutable de Eventos (Forensic Logging)
- Todas las transacciones financieras y decisiones críticas de agentes se firman con un **Hash SHA-256**.
- Se utiliza una estructura de "encadenamiento" (Chaining) donde cada log contiene el hash del log anterior, detectando cualquier intento de manipulación.

## 3. Seguridad de Agentes AI
- **Sandboxing:** Los agentes ejecutan código en entornos aislados con permisos restringidos.
- **Control de Acceso entre Agentes:** Un agente solo puede llamar a otro si tiene la autorización explícita definida en la matriz de gobernanza.
- **Validación de Nonce:** Cada solicitud de agente incluye un número de un solo uso para prevenir ataques de repetición.

## 4. Infraestructura Segura

### 4.1 Segmentación de Red
- **VPC (Virtual Private Cloud):** Los servicios de backend y bases de datos residen en subredes privadas sin acceso directo desde internet.
- **Firewalls de Aplicación (WAF):** Protección contra ataques comunes (SQLi, XSS, DDoS).

### 4.2 Rate Limiting (Limitación de Tasa)
Implementado en el `SecurityHardeningMiddleware`:
- **Usuarios Estándar:** 250 peticiones por minuto.
- **Administradores:** 300 peticiones por minuto.
- Protección automática con bloqueo de IP tras múltiples intentos fallidos.

## 5. Auditoría y Trazabilidad Distribuida
- **Trace ID:** Cada solicitud recibe un ID de seguimiento único que viaja a través de todos los microservicios y agentes.
- **Auditoría Ex-Post:** Sistema de revisión automática que busca inconsistencias en los logs de forma diaria.
