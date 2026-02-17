# Modelo de Gobierno y Trazabilidad - Sistema SARITA

## 1. Comité Virtual de Decisión (CVD)
El CVD es un marco de gobernanza algorítmica y humana que supervisa el comportamiento del sistema.

### 1.1 Composición
- **Nivel Algorítmico:** Agente Auditor + Agente de Cumplimiento.
- **Nivel Humano:** Administradores del Sistema (Súper Usuarios).

### 1.2 Matriz RACI del Sistema

| Actividad / Proceso | Usuario Final | Agente Especialista | Agente Coordinador | Agente Auditor | Admin Humano |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Operación Diaria | R | A | S | I | I |
| Transacción Financiera | I | R | A | C | I |
| Cambio de Configuración | I | I | C | R | A |
| Resolución de Conflictos | I | I | R | C | A |
| Auditoría de Logs | I | I | I | R | A |

*R: Responsible, A: Accountable, C: Consulted, I: Informed*

---

## 2. Protocolos de Gestión

### 2.1 Escalamiento Automático
Si un agente encuentra una situación que supera su límite de autoridad (ej. transacción de alto valor o error sistémico), se activa el siguiente flujo:
1. **Nivel 1:** Intento de resolución por Agente Coordinador.
2. **Nivel 2:** Bloqueo preventivo y notificación al Agente de Riesgo.
3. **Nivel 3:** Solicitud de intervención humana (Admin) vía Dashboard de Alertas.

### 2.2 Protocolo de Conflicto entre Agentes
Cuando dos agentes tienen directivas contradictorias:
1. Se invoca al **Agente Auditor** para revisar las reglas de negocio base.
2. Prevalece la directiva del agente con mayor **Nivel de Autoridad** (Jerarquía Militar).
3. Si los niveles son iguales, se aplica la política de "Seguridad Primero": se deniega la acción y se registra el conflicto.

---

## 3. Control de Cambios (Change Control)

### 3.1 Versionado Obligatorio
- **Código:** SemVer (Semantic Versioning) para todos los microservicios.
- **Modelos de Datos:** Migraciones versionadas y rastreadas en la DB.
- **Reglas de Agentes:** Versionado de Prompts y lógica de decisión.

### 3.2 Registro de Cambios (Audit Trail)
Cada cambio en el sistema (configuración, código, datos) debe estar vinculado a un:
- **ID de Cambio.**
- **Autor (Humano o Agente).**
- **Evaluación de Impacto** previa al despliegue.

---

## 4. Definición de Identificadores Globales Únicos
Se establece el uso obligatorio de **UUID v4** para todas las entidades del sistema para garantizar la unicidad en entornos distribuidos y facilitar la sincronización multi-región.

## 5. Política de Retención y Archivo
- **Logs Operativos:** 1 año en línea, 5 años en almacenamiento frío.
- **Transacciones Financieras:** 10 años (según normativa legal).
- **Evidencia Digital:** Almacenamiento inmutable vinculado a la transacción.
