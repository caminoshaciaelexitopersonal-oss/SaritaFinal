# ALINEACIÓN DE CUMPLIMIENTO GLOBAL (GLOBAL COMPLIANCE ALIGNMENT)

**Versión:** 1.0 (Fase Final Z)
**Estado:** DECLARACIÓN DE DISEÑO
**Alcance:** Seguridad, Privacidad y Gobernanza de IA.

---

## 1. ALINEACIÓN CON MARCOS DE SEGURIDAD (ISO 27001 / NIST)

SARITA incorpora principios de seguridad por diseño alineados con estándares globales:

*   **Identidad y Acceso:** Implementación de RBAC (Role-Based Access Control) con segregación estricta de funciones entre las tres vías.
*   **Criptografía:** Aislamiento de "Tenants" mediante sal de cifrado única por compañía (`apps.companies.models.CompanyEncryptionKey`).
*   **Trazabilidad:** Bitácora inmutable de auditoría forense con encadenamiento de hashes para prevenir la alteración de registros.
*   **Resiliencia:** Implementación de Modo Ataque (System Freeze) para la contención inmediata de amenazas detectadas.

## 2. GOBERNANZA DE INTELIGENCIA ARTIFICIAL (EU AI ACT / OECD)

SARITA se posiciona como un sistema de **IA de Riesgo Limitado/Alto** (dependiendo del módulo) y cumple con los siguientes principios:

*   **Supervisión Humana:** El "Governance Kernel" asegura que ningún agente ejecute acciones críticas (Nivel 2) sin validación de políticas humanas.
*   **Explicabilidad (XAI):** Cada decisión de un "Funcionario Digital" es registrada con una justificación en lenguaje humano (5-point decision chain).
*   **Soberanía de Datos:** Los modelos de IA no entrenan con datos sensibles de las empresas sin consentimiento explícito; se usan agentes especializados por dominio.
*   **Derecho a la Intervención:** El "Kill Switch" global permite a la autoridad soberana detener cualquier proceso automatizado instantáneamente.

## 3. PRIVACIDAD Y PROTECCIÓN DE DATOS (GDPR / LEY 1581)

*   **Minimización:** Solo se recolectan los datos necesarios para la operación y el cumplimiento normativo.
*   **Propiedad del Dato:** El sistema reconoce al Prestador como dueño de su información operativa y al Gobierno como custodio de la información pública.
*   **Derechos ARCO:** Interfaces preparadas para el ejercicio de derechos de acceso, rectificación y cancelación por parte de los ciudadanos.

## 4. ESTADO DE CUMPLIMIENTO ACTUAL

| Estándar | Estado | Evidencia en el Sistema |
| :--- | :--- | :--- |
| ISO 27001 (Seguridad) | Alineado | ForensicSecurityLog, RBAC, EncryptionKeys. |
| EU AI Act (IA) | Alineado | GovernanceKernel, XAI, Kill Switch. |
| GDPR (Privacidad) | Alineado | ToS Consent, Data Isolation per Tenant. |
| AI Ethics (OECD) | Alineado | Declaración de Autonomía Controlada. |

---
**"SARITA no solo cumple la ley; implementa la ley en su propio código."**
