# MODELO DE ESCALAMIENTO POR NODOS SOBERANOS
**Fase 9: Expansión Territorial y Descentralización**

## 1. ARQUITECTURA DE NODOS
Sarita no es una aplicación monolítica; es una red federada de nodos independientes pero alineados normativamente.

### 1.1 Tipología de Nodos
- **Nodo Nacional (Hub de Políticas):** Emite el set base de reglas de gobernanza y leyes nacionales. Actúa como autoridad suprema en conflictos.
- **Nodo Departamental (Regional):** Coordina múltiples municipios, gestiona rutas regionales y supervisa cumplimiento táctico.
- **Nodo Municipal (Operación Local):** Es el nodo de contacto directo con prestadores y turistas. Posee autonomía para decretos locales.

## 2. MECANISMO DE REPLICACIÓN
Cada nuevo nodo se despliega con un **Kernel Local** que hereda las políticas del nodo superior inmediato (Sync Hacia Abajo) pero no puede modificarlas (Herencia Protegida).

## 3. AISLAMIENTO Y SEGURIDAD
- **Data Sovereignty:** Los datos transaccionales de una alcaldía NO residen en el mismo silo que otra, evitando fugas de información cruzada.
- **Encryption Tenants:** Cada nodo posee su propio `CompanyEncryptionKey` derivado de un secreto jurisdiccional.

---
**Escalamiento Seguro para Infraestructura Crítica.**
