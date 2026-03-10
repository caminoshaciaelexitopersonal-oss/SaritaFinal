# Auditoría de Seguridad Mobile - SARITA v1.0

## 1. Protección de Credenciales

Se ha verificado el blindaje de la sesión del usuario.
*   **Almacenamiento**: Migración total a `expo-secure-store`. Los tokens de acceso y refresh se guardan utilizando el Keychain (iOS) y Keystore (Android).
*   **Invalidación**: El sistema detecta fallos de renovación y fuerza el cierre de sesión para prevenir accesos no autorizados.

## 2. Seguridad en las Comunicaciones

*   **HTTPS**: Todas las llamadas al backend se realizan bajo túneles TLS seguros.
*   **Token Rotation**: Implementación de refresh tokens con vida corta para minimizar la ventana de exposición.
*   **MFA Support**: La app soporta el flujo de autenticación de dos factores requerido por el backend.

---
**Certificado**: Jules, Lead Software Engineer.
