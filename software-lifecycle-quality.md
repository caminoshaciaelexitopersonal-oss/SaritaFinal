# Gestión de Versiones y Calidad SARITA v1.0

## 1. Versionado Semántico (SemVer)
La plataforma utiliza el estándar **MAJOR.MINOR.PATCH** para comunicar cambios de forma predecible.

*   **MAJOR**: Cambios incompatibles con la API anterior.
*   **MINOR**: Nuevas funcionalidades compatibles con la versión actual.
*   **PATCH**: Correcciones de errores y parches de seguridad.

## 2. Estrategia de Lanzamientos (Release Strategy)
*   **Canary Deployment**: Los cambios se liberan primero al 5% de los usuarios.
*   **Freeze Periods**: Bloqueo de despliegues durante temporadas de alta transaccionalidad regional (Fines de semana festivos).
*   **Automated Rollback**: Reversión automática si el error_rate supera el 1% tras un deploy.

## 3. Estándares de Calidad y Deuda Técnica
*   **Code Review**: Mínimo 2 aprobaciones senior para cambios en el núcleo contable.
*   **Static Analysis**: Integración mandatoria de SonarQube y Linters.
*   **Coverage Meta**: Mantener > 85% de cobertura en todos los microservicios.

---
**Garantizando la excelencia técnica a largo plazo.**
*Jules, Lead AI & Software Architect.*
