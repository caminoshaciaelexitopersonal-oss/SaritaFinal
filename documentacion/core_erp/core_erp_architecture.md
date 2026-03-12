# Arquitectura Core ERP - SARITA

## 💎 Visión General
El núcleo `core_erp` constituye la infraestructura empresarial base para todo el ecosistema SARITA. Ha sido diseñado bajo el principio de **Aislamiento de Dominio**, lo que permite que tanto el Administrador de Plataforma como los Prestadores compartan la misma lógica de negocio financiera sin acoplamiento de datos.

## 🏗️ Capas de la Arquitectura

### 1. Base (Abstract Models)
Localización: `apps/core_erp/base/`
Contiene las clases abstractas que definen el "contrato" de datos:
- `BaseAccount`: Código, Nombre, Tipo.
- `BaseJournalEntry`: Fecha, Referencia, Descripción, Estado de Registro.
- `BaseAccountingTransaction`: Débito, Crédito.
- `BaseInvoice`: Número, Fecha Emisión, Fecha Vencimiento.

### 2. Motores (Business Engines)
Localización: `apps/core_erp/accounting/`, `apps/core_erp/billing/`, etc.
Implementan la lógica procedimental obligatoria:
- `AccountingEngine`: Validación de partida doble, cierre de asientos.
- `BillingEngine`: Cálculo de totales e impuestos.

### 3. Contratos e Interfaces
Localización: `apps/core_erp/contracts/`
Define las interfaces `ABC` para asegurar la paridad funcional.

## 🔄 Flujo de Implementación
Para utilizar el núcleo, los módulos de dominio (`admin_plataforma`, `prestadores`) deben:
1. Heredar de las clases base en `core_erp.base.base_models`.
2. Delegar el procesamiento de datos a los motores correspondientes.
3. Respetar la versión global `CORE_ERP_VERSION` para evitar inconsistencias en caliente.

## ⚖️ Reglas de Oro
- **Prohibición de FK externas:** El núcleo no puede referenciar modelos fuera de `core_erp`.
- **Agnosticismo de Tenant:** El núcleo no conoce el concepto de "inquilino" o "empresa", solo opera sobre objetos financieros.
- **Trazabilidad:** Toda operación crítica debe pasar por un `Engine`.
