# ARQUITECTURA DE AGENTES IA: SARITA v1.0
**Lead Architect:** Jules (Senior AI Software Engineer)
**Date:** March 2026

## 1. Desacoplamiento de Capas
La arquitectura de inteligencia artificial de SARITA ha sido refactorizada para cumplir con el principio de responsabilidad única y aislamiento de persistencia.

### Diagrama de Interacción
```text
[ Agente IA (N1-N7) ]
        ↓
[ Application Service ]  ← (Reglas de Negocio / Orquestación)
        ↓
[ Repository Layer ]     ← (Acceso a Datos / ORM Django)
        ↓
[ Database ]             ← (PostgreSQL / SQLite)
```

## 2. Responsabilidades por Capa

### 2.1 Agentes IA
- **Misión:** Análisis de lenguaje natural, toma de decisiones estratégicas y planificación de tareas.
- **Restricción:** No pueden importar modelos de Django ni ejecutar consultas SQL directas.

### 2.2 Application Services
- **Misión:** Encapsular la lógica de negocio, validaciones y coordinación de múltiples repositorios.
- **Salida:** Estructura `ServiceResult` (success, data, error).

### 2.3 Repositorios
- **Misión:** Abstraer el ORM de Django. Proporcionar métodos limpios de consulta y persistencia.
- **Aislamiento:** Permite cambiar el motor de base de datos sin afectar a los agentes.

## 3. Sistema de Trazabilidad
Cada interacción de un agente con la capa de servicios es registrada por el `AgentExecutionLogger`, permitiendo una auditoría forense de las decisiones autónomas tomadas por el sistema.

---
**Resultado Estratégico:** Esta arquitectura garantiza que SARITA pueda evolucionar hacia una infraestructura de microservicios sin reescribir la inteligencia de los agentes.
