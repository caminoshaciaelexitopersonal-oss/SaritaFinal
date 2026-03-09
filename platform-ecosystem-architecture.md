# Arquitectura del Ecosistema de Plataforma SARITA v1.0

## 1. Visión de Plataforma Abierta
SARITA evoluciona hacia un ecosistema extensible, permitiendo que desarrolladores externos y socios estratégicos construyan soluciones sobre el núcleo soberano regional.

### 1.1 Capas de Interoperabilidad
*   **Public APIs Layer**: Interfaz RESTful para el desarrollo de aplicaciones de terceros (Turismo, Finanzas, Logística).
*   **Partner APIs**: Endpoints de alta sensibilidad para integración profunda con gobiernos y entidades bancarias.
*   **Internal APIs**: Comunicación privada entre microservicios (gRPC).

## 2. Estándares y Gobernanza de API

### 2.1 Diseño RESTful y Versionado
*   **Estandarización**: Todas las APIs siguen el estándar OpenAPI 3.0.
*   **Versionado URI**: `/api/v1/`, `/api/v2/` para garantizar la compatibilidad hacia atrás de las integraciones externas.

### 2.2 Autenticación y Autorización
*   **Desarrolladores Externos**: Implementación de **OAuth 2.0 (Authorization Code Flow)** con gestión de Scopes (`read:inventory`, `write:sales`).
*   **Integraciones Simples**: Soporte para **API Keys** con rotación mandatoria cada 90 días.

## 3. Rate Limiting y Control de Abuso
Gestión centralizada en el API Gateway (Kong):
*   **Tier Free**: 1,000 req/día.
*   **Tier Pro/Partner**: 100,000 req/día.
*   **Detección de Anomalías**: Bloqueo automático ante patrones de scraping o ataques de denegación.

---
**Arquitectura aprobada para crecimiento impulsado por terceros.**
*Jules, Lead AI & Ecosystem Architect.*
