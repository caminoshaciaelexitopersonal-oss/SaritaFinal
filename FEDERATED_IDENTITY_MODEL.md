# MODELO DE IDENTIDAD FEDERADA (FEDERATED IDENTITY MODEL)

**Versión:** 1.0 (Fase Z-INT)
**Estrategia:** Identidad Local con Reconocimiento Diplomático.
**Principio:** No existe un usuario "Global".

---

## 1. PRINCIPIO DE RESIDENCIA DE IDENTIDAD
SARITA rechaza la idea de una base de datos centralizada de usuarios internacionales. La identidad de un ciudadano o funcionario reside **exclusivamente** en su Nodo Nacional de origen.

## 2. MECANISMO DE ACCESO FEDERADO (DIPLOMATIC PASS)
Cuando un usuario del País A necesita interactuar con servicios permitidos del País B (bajo un TID activo):

1.  **Solicitud Local:** El usuario se autentica en su Nodo Nacional (País A).
2.  **Emisión de Pasaporte Digital:** El Nodo A genera un token temporal firmado por el IKERNEL (País A).
3.  **Validación Diplomática:** El IKERNEL del País B verifica la firma del Nodo A contra su repositorio de certificados autorizados.
4.  **Sombra de Usuario (Shadow User):** El País B crea un registro temporal (volátil) que representa al usuario extranjero sin almacenar sus datos privados.
5.  **Expiración:** El acceso caduca automáticamente al finalizar la sesión o al expirar el token del TID.

## 3. AUTENTICACIÓN MUTUA (MTLS)
La comunicación entre los IKERNEL de diferentes países se realiza mediante **Mutual TLS**:
- Cada Nodo Nacional posee un certificado raíz emitido por su propia autoridad soberana.
- El intercambio de llaves públicas ocurre únicamente durante la formalización del Tratado (TID).
- Cualquier petición sin un certificado mutuo válido es rechazada en la capa de red (Capa 4).

## 4. AUDITORÍA DE IDENTIDAD
Cada acción realizada por un "Shadow User" extranjero es registrada con:
- Identificador de Nodo Origen.
- Referencia al TID que autoriza la acción.
- Hash de identidad (sin revelar el nombre real del usuario extranjero).

## 5. PROHIBICIÓN DE CONTROL CRUZADO
Un SuperAdmin del País A **nunca** podrá tener permisos administrativos en el Nodo B. Las herramientas de gestión (Vía 1) son exclusivas para ciudadanos con mandato legal dentro de su jurisdicción nacional.

---
**"La identidad digital soberana significa que tu país es el único que sabe quién eres."**
