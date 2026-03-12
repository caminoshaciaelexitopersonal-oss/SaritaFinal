# ESPECIFICACIÓN DEL KERNEL DE INTEROPERABILIDAD (IKERNEL SPEC)

**Versión:** 1.0 (Fase Z-INT)
**Módulo:** `apps.interoperability_kernel`
**Rol:** Controlador Diplomático de Flujos Internacionales.

---

## 1. PROPÓSITO TÉCNICO
El IKERNEL es el único componente autorizado para gestionar la comunicación con nodos externos. Actúa como un "Consulado Digital" que valida pasaportes de datos y aplica los términos de los Tratados de Interoperabilidad (TID).

## 2. FUNCIONES CORE

### 2.1 Validador de Tratados (TID Enforcement)
*   **Función:** Carga y verifica la validez temporal y técnica de los contratos TID en formato JSON.
*   **Acción:** Bloquea cualquier petición si no existe un TID activo para el Nodo Origen/Destino especificado.

### 2.2 Filtro de Exportación (Nivel de Clasificación)
*   **Función:** Inspecciona los eventos generados por el Nodo Nacional antes de su salida.
*   **Acción:** Elimina campos no autorizados según la `DATA_CLASSIFICATION_POLICY` (ej. borrado de PII en Nivel 2).

### 2.3 Firma Diplomática (Signed Exchange)
*   **Función:** Firma criptográficamente cada paquete de salida usando la llave privada del tratado.
*   **Acción:** Asegura al nodo receptor que el dato es auténtico y no ha sido manipulado en tránsito.

### 2.4 Registro Diplomático (Diplomatic Audit Log)
*   **Función:** Bitácora independiente del intercambio internacional.
*   **Campos:** ID de Tratado, IP Origen/Destino, Hash de Paquete, Resultado (Habilitado/Bloqueado).

## 3. KILL SWITCH INTERNACIONAL
El IKERNEL implementa un mecanismo de interrupción inmediata:
1. **Manual:** El SuperAdmin local pulsa "Revocar Cooperación".
2. **Automático:** Si el nodo remoto devuelve señales de ataque (ej. 403 masivos o patrones de reconocimiento).
3. **Efecto:** Cierre total de sockets y revocación de certificados federados.

## 4. INTEGRACIÓN CON AGENTES SARITA
Los Coroneles de un Nodo Nacional pueden enviar solicitudes al IKERNEL para intercambiar señales de inteligencia:
- **Coronel Defensa A:** "Solicito patrones de ataque detectados por Nodo B en las últimas 24h".
- **IKERNEL A:** Verifica el tratado TID de seguridad y ejecuta la petición al IKERNEL B.

---
**"El IKERNEL no es un puente; es una aduana digital que protege la soberanía."**
