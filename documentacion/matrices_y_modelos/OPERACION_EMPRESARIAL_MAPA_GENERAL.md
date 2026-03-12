# OPERACION EMPRESARIAL MAPA GENERAL - SARITA

**Fecha:** 24 de Mayo de 2024
**Estado:** Certificado

## 1. EJES OPERATIVOS (FRONTEND ↔ BACKEND)

| Eje | Componente Frontend | Mapeo Backend | Estado Real |
| :--- | :--- | :--- | :--- |
| **Gestión Operativa Core** | `gestion-operativa/page.tsx` | `prestadores.mi_negocio.gestion_operativa` | ✅ REAL |
| **Gestión Contable** | `gestion-contable/page.tsx` | `prestadores.mi_negocio.gestion_contable` | ✅ REAL |
| **Gestión Financiera** | `gestion-financiera/page.tsx` | `prestadores.mi_negocio.gestion_financiera` | ✅ REAL |
| **Gestión Archivística** | `gestion-operativa/genericos/documentos` | `prestadores.mi_negocio.gestion_archivistica` | ✅ REAL |
| **Gestión de Nómina** | `gestion-contable/nomina/page.tsx` | `prestadores.mi_negocio.gestion_contable.nomina` | ⚠️ INTEGRADO |
| **Seguridad y Salud (SST)** | `gestion-operativa/sst/page.tsx` | `sarita_agents...sg_sst` | 🟡 PLANTILLA |

## 2. FLUJO DE OPERACIÓN INTEGRADA
1.  **Activación Operativa:** Tras la venta, se genera una `Operación Comercial` que dispara la asignación de recursos en los módulos especializados.
2.  **Ejecución Especializada:** Gestión de habitaciones (Hoteles), mesas (Restaurantes) o rutas (Guías).
3.  **Soporte Laboral:** Registro de empleados y liquidación de nómina vinculada a la operación.
4.  **Cierre Contable:** Cada gasto operativo (insumos, nómina) genera un asiento automático en el Libro Diario.
5.  **Trazabilidad Archivística:** Carga de evidencias (fotos, PDFs, contratos) con sellado de integridad SHA-256.

## 3. ESTADO DE MADUREZ
El ERP de Sarita presenta una madurez técnica avanzada en los módulos financieros y contables, mientras que los módulos especializados de operación física (Hoteles, Restaurantes) se encuentran en fase de **Ejecución Real Asistida** (UI preparada con mapeo a modelos backend existentes).
