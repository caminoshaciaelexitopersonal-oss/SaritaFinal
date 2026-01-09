# CIERRE DE PRODUCCIÓN (FREEZE FUNCIONAL)

Este documento declara el cierre funcional del sistema "Sarita" y sirve como un registro de su estado final antes del paso a producción. A partir de este punto, no se realizarán más cambios funcionales, arquitectónicos ni de modelos.

## 1. Alcance Funcional Final del Sistema

El sistema "Sarita" se entrega como una plataforma de turismo de "triple vía":

1.  **Gobernanza:** Permite a las entidades administradoras (ej. Secretarías de Turismo) gestionar el contenido fundamental del destino, incluyendo Atractivos Turísticos, Rutas, y Publicaciones (Noticias/Eventos). Incluye un módulo para la verificación de cumplimiento de los prestadores de servicios.
2.  **Empresarios (Prestadores):** Proporciona un panel de control ("Mi Negocio") que incluye un ERP con cinco módulos para la gestión de su operación.
3.  **Turistas:** Ofrece un portal público para descubrir el destino, consultar el directorio de prestadores y artesanos, y planificar su viaje.

## 2. Módulos Incluidos (ERP "Mi Negocio")

Los siguientes cinco módulos del ERP se consideran funcionalmente completos en su estructura básica:

1.  **Gestión Operativa:** Es la fuente de la verdad para los datos maestros (Perfil del Prestador, Productos/Servicios, Clientes).
2.  **Gestión Comercial:** Gestiona el ciclo de ventas, desde la creación de una `OperacionComercial` hasta la generación de una `FacturaVenta`.
3.  **Gestión Contable:** Incluye un sistema de contabilidad de partida doble (`JournalEntry`), gestión de inventario (`MovimientoInventario`) y plan de cuentas (`ChartOfAccount`).
4.  **Gestión Archivística:** Proporciona un servicio transversal para la gestión documental estructurada, con versionamiento y preparación para notarización en blockchain.
5.  **Gestión Financiera:** Define las `CuentasBancarias` y `OrdenesDePago` para la gestión de tesorería.

## 3. Decisiones Irreversibles (Arquitectura Congelada)

1.  **Arquitectura de Dominios Desacoplados:** Se mantiene la arquitectura donde los módulos de negocio (`gestion_comercial`, `gestion_contable`, etc.) están desacoplados a nivel de base de datos, usando `UUIDField` para las referencias cruzadas.
2.  **Patrón de Orquestación de Servicios:** La lógica de negocio que involucra a múltiples dominios se orquesta en una capa de servicio (ej. `FacturacionService`), que es responsable de coordinar las llamadas a otros servicios. Esta decisión es final.
3.  **No Más Migraciones de Modelos:** La estructura de la base de datos se congela. No se añadirán, eliminarán ni modificarán campos en los modelos existentes.

## 4. Riesgos Conocidos Aceptados

Se pasa a producción con conocimiento y aceptación de los siguientes puntos de deuda técnica:

1.  **Acoplamiento en Capas de Serialización y Señales:** Ciertos componentes (`serializers.py` en `gestion_comercial`, `signals.py` en `inventario`) están fuertemente acoplados, importando modelos de otros dominios directamente. Aunque funcional, contradice la arquitectura de dominios desacoplados y debe ser refactorizado en un futuro ciclo de mantenimiento, no ahora.
2.  **Advertencia Persistente de `django-allauth`:** La advertencia `(account.W001)` no pudo ser resuelta a pesar de múltiples intentos. No afecta la funcionalidad y se acepta como un problema menor a investigar en el futuro.
3.  **Lógica de DIAN y SGA Incompleta:** Las integraciones con servicios externos como la DIAN y el archivado (SGA) dentro del `FacturacionService` son stubs o están incompletas y fallan silenciosamente. El flujo de negocio principal (creación de factura y asiento contable) funciona, pero estas integraciones no.
4.  **Vulnerabilidades de NPM:** El frontend tiene vulnerabilidades de nivel "high" y "moderate" que no pudieron ser resueltas sin realizar una actualización de alto riesgo del framework `next`. Se acepta el riesgo de estas vulnerabilidades a cambio de la estabilidad de la versión actual.
