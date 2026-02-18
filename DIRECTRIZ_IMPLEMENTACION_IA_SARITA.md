# DIRECTRIZ OFICIAL: IMPLEMENTACIÓN INTEGRAL DE AGENTES IA (SADI-SARITA)

**Para:** Equipo de Desarrollo e Integración de IA
**Carácter:** ESTRATÉGICO - OBLIGATORIO
**Visión:** Lograr que cada flujo de negocio, transacción y dato en el sistema Sarita sea observado, validado o ejecutado por una entidad de Inteligencia Artificial especializada.

---

## 1. ARQUITECTURA DE COBERTURA TOTAL (6 NIVELES)

La implementación debe seguir la jerarquía militar establecida en `backend/apps/sarita_agents/agents/`:

1.  **N1 - Soldados (Ejecutores Granulares):** Automatización de tareas repetitivas (ej: actualizar stock, enviar un email, hashear un documento).
2.  **N2 - Sargentos (Interfaz de Negocio):** Actúan como el "puente" entre la IA y los `Services` de Django. Ningún agente debe tocar la DB directamente sin un Sargento.
3.  **N3 - Tenientes (Líderes de Módulo):** Responsables de un submódulo (ej: Facturación, Reservas, Nómina).
4.  **N4 - Capitanes (Coordinadores):** Orquestan flujos entre múltiples tenientes (ej: el Capitán de Cierre vincula Contabilidad con Finanzas).
5.  **N5 - Coroneles (Soberanos de Dominio):** Gobiernan áreas completas (Prestadores, Gobierno, Turistas).
6.  **N6 - General (Sadi/Sarita):** El orquestador central que recibe comandos de voz/texto y delega a los Coroneles.

---

## 2. DESPLIEGUE POR RINCONES DEL SISTEMA

### 🔹 Rincón Comercial (Marketing & Ventas)
- **Agentes Requeridos:**
    - `TenienteCalificador`: Analiza el perfil digital del prospecto.
    - `TenienteCierre`: (Ya implementado) Ejecuta la conversión real y creación de perfiles.
    - `SoldadoUpselling`: Detecta oportunidades de planes superiores basados en el uso del sistema.

### 🔹 Rincón Operativo (Mi Negocio)
- **Agentes Requeridos:**
    - `TenienteLogistico`: Optimiza la asignación de habitaciones y mesas en tiempo real.
    - `TenienteArtesano`: (Prioridad) Vincula la producción del taller con el inventario de ventas automáticamente.
    - `SoldadoMantenimiento`: Predice fallos en activos basados en registros de uso.

### 🔹 Rincón Contable y Financiero
- **Agentes Requeridos:**
    - `CapitanAuditor`: Realiza conciliación bancaria vs Monedero Soberano cada hora.
    - `TenienteImpuestos`: Calcula proyecciones de IVA y retenciones en tiempo real.
    - `SoldadoRiskScore`: Alimenta el `EvaluationEngine` con datos de comportamiento transaccional.

### 🔹 Rincón Archivístico (Gobierno de Datos)
- **Agentes Requeridos:**
    - `TenienteNotario`: Asegura que cada factura y contrato tenga su hash SHA-256 en la "Blockchain" interna.
    - `SoldadoClasificador`: Lee PDFs subidos y extrae metadatos mediante OCR/Vision para categorización automática.

---

## 3. PROTOCOLO DE INTEGRACIÓN (SADI-INTEROP)

Para que un rincón se considere "Cubierto por IA", debe cumplir:

1.  **Observabilidad:** El agente debe recibir un `signal` de Django ante cada cambio relevante en su dominio.
2.  **Memoria Semántica:** Cada decisión importante debe consultarse con el `MemoryService` para buscar precedentes.
3.  **Gobernanza:** Toda acción ejecutiva (N3 hacia arriba) debe registrar un `GovernanceAuditLog` con el `RiskScore` calculado.
4.  **Interfaz de Usuario:** El dashboard debe mostrar "Sugerencias de la IA" basadas en las misiones completadas por los agentes.

---

## 4. MAPA DE RUTA DE IMPLEMENTACIÓN

- **Fase 1 (Inmediata):** Población de Sargentos en todos los módulos de `Prestadores`.
- **Fase 2:** Activación de Tenientes de Control (Auditoría en tiempo real).
- **Fase 3:** Integración de comandos de voz mediante el General para control total "Hands-Free".

**"En Sarita, ningún dato nace, se mueve o muere sin que un agente lo sepa."**
