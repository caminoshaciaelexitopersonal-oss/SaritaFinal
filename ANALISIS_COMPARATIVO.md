# Análisis Comparativo del Sistema Sarita

Este documento detalla el análisis de brechas (gap analysis) entre el estado actual de los componentes del sistema Sarita y la funcionalidad completa presente en el código fuente.

## Resumen Ejecutivo

El sistema Sarita, tanto en su backend (Django) como en su frontend (Next.js), se encuentra en un estado de desarrollo muy avanzado. La lógica de negocio para un sistema ERP completo (comercial, contable, financiero, inventario, etc.) está implementada a un nivel de producción. Sin embargo, el sistema está **inoperativo** debido a una brecha fundamental que no es de desarrollo, sino de **configuración y activación**.

La causa raíz de que el sistema no funcione es que los módulos de gestión del backend, a pesar de estar completamente codificados, nunca fueron "encendidos":
1.  **No hay migraciones de base de datos** para los modelos de los módulos de gestión.
2.  **Las APIs no están registradas** en los archivos de URLs, por lo que son inaccesibles.

El frontend está construido para consumir estas APIs y, al no encontrarlas, se queda en un estado de "carga infinita", que es el síntoma principal del problema. El trabajo requerido es, por lo tanto, un proceso de integración y activación, no de creación de funcionalidades desde cero.

---

## I. Análisis de Brechas del Backend

| Componente/Módulo | Estado Actual | Funcionalidad Esperada (según el código) | Brecha / Acciones Requeridas |
| :--- | :--- | :--- | :--- |
| **Gestión Comercial** | Modelos (`FacturaVenta`, `ReciboCaja`) y APIs (`ViewSet`s) 100% implementados con lógica de negocio robusta e integración contable. **Inactivo.** | Sistema completo de facturación, registro de pagos y gestión de clientes. | 1. Generar y ejecutar migraciones. <br> 2. Registrar los `ViewSet`s en `mi_negocio/urls.py`. <br> 3. Asegurar que las dependencias (`contabilidad`, `financiera`) estén activas. |
| **Gestión Contable** | "Super-aplicación" con 8 sub-módulos (Contabilidad, Compras, Inventario, Activos Fijos, etc.). El núcleo contable (`JournalEntry`, `ChartOfAccount`) y de inventario (`Producto`) está 100% implementado. **Inactivo.** | Un sistema ERP contable completo, con contabilidad de doble entrada, gestión de inventario, compras y más. | 1. Generar y ejecutar migraciones para todos los sub-módulos. <br> 2. Registrar las APIs de cada sub-módulo. <br> 3. Resolver `ImportError` que impiden las migraciones. |
| **Gestión Financiera** | Modelos (`CuentaBancaria`, `TransaccionBancaria`) y APIs implementados con lógica para gestión de saldos. **Inactivo.** | Sistema de tesorería para gestionar cuentas bancarias, ingresos y egresos. | 1. Generar y ejecutar migraciones. <br> 2. Registrar los `ViewSet`s en `mi_negocio/urls.py`. |
| **Gestión Archivística** | Esqueleto del módulo presente. | (Por definir en análisis más profundo). | (Por definir). |
| **Gestión Operativa** | Módulos genéricos como `Perfil` y `Clientes` están definidos. Parcialmente activo. | Base para la gestión de la información del prestador de servicios. | Completar la integración y activación de todos sus componentes. |

---

## II. Análisis de Brechas del Frontend

| Componente/Módulo | Estado Actual | Funcionalidad Esperada (según el código) | Brecha / Acciones Requeridas |
| :--- | :--- | :--- | :--- |
| **Páginas de Módulos** | Componentes de React (`page.tsx`) para cada módulo (`facturas-venta`, etc.) están completamente construidos, con tablas, formularios y gestión de estado. | Interfaces de usuario funcionales para interactuar con todas las funcionalidades del ERP del backend. | Las páginas están listas, pero fallan porque las llamadas a la API que realizan no reciben respuesta. No se requiere trabajo en los componentes en sí. |
| **Hook `useMiNegocioApi`** | El hook central de la aplicación está 100% desarrollado. Contiene definiciones de tipos (TypeScript) y funciones de llamada a API (Axios) para **todos** los endpoints del backend. | Un "SDK" del frontend para el backend, que permite a los componentes interactuar de forma segura y tipada con la API. | El hook es correcto. La brecha es que las URLs a las que apunta (`/v1/mi-negocio/...`) devuelven errores 404 porque las APIs del backend no están registradas. |
| **Estado General** | La aplicación se queda en un "círculo de carga infinito". | Una experiencia de usuario fluida donde los datos se cargan y se muestran en las tablas y formularios. | El estado de carga infinito es un **síntoma**, no la enfermedad. Se resolverá automáticamente una vez que el backend esté activo y las llamadas a la API comiencen a devolver datos en lugar de errores. |
