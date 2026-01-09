# Documento de Levantamiento de Requisitos – Sistema de Gestión Archivística (SGA)

---

## Objetivo

El propósito de este documento es definir, en conjunto con ustedes (el cliente), la **columna vertebral** de nuestro Sistema de Gestión Archivística. Las respuestas que recopilemos aquí determinarán cómo se clasifican, almacenan y protegen todos los documentos generados por el ERP "Sarita", garantizando su integridad, trazabilidad y validez legal a largo plazo.

---

## 1. Validación de Áreas de Negocio (Tipos de Proceso)

El primer nivel de organización son las grandes áreas funcionales de su negocio. Proponemos la siguiente lista inicial. Por favor, valídenla, corrijan o añadan las que consideren necesarias.

**Propuesta de Áreas de Negocio:**

*   [ ] Contabilidad
*   [ ] Finanzas
*   [ ] Comercial
*   [ ] Operaciones
*   [ ] Legal
*   [ ] Talento Humano
*   [ ] Gerencia / Administración

**Preguntas para el Cliente:**
*   ¿Son correctas estas áreas para su operación?
*   ¿Falta alguna área importante?
*   ¿Deberíamos renombrar alguna de ellas para que se ajuste mejor a su organización?

---

## 2. Definición de Procesos Específicos

Dentro de cada área de negocio, necesitamos identificar los procesos concretos que generan documentos. A continuación, proporcionamos una tabla con ejemplos. Por favor, complétenla con los procesos reales de su empresa.

| Área de Negocio (Validada en el punto 1) | Procesos Específicos dentro del Área (Por favor, completar) |
| :--- | :--- |
| **Contabilidad** | 1. `Facturación` <br> 2. `Nómina` <br> 3. `Cierres Contables` <br> 4. `Declaraciones de Impuestos` <br> 5. *... (añadir otros si aplica)* |
| **Finanzas** | 1. `Pagos a Proveedores` <br> 2. `Recaudos de Clientes` <br> 3. `Conciliaciones Bancarias` <br> 4. *... (añadir otros si aplica)* |
| **Comercial** | 1. `Ventas y Cotizaciones` <br> 2. `Gestión de Contratos` <br> 3. *... (añadir otros si aplica)* |
| **Operaciones** | 1. `Gestión de Reservas` <br> 2. `Control de Inventario` <br> 3. `Gestión de Eventos` <br> 4. `Logística de Transporte` <br> 5. *... (añadir otros si aplica)* |
| **Legal** | 1. `Gestión de Pólizas` <br> 2. `Conceptos Jurídicos` <br> 3. *... (añadir otros si aplica)* |
| **Talento Humano** | 1. `Contratación de Personal` <br> 2. `Gestión de Novedades (Incapacidades, etc.)` <br> 3. *... (añadir otros si aplica)* |

---

## 3. Catálogo de Documentos y Nivel de Criticidad (El Paso Más Importante)

Aquí definiremos cada tipo de documento que el sistema debe gestionar y su nivel de importancia. Esto determinará si un documento requiere la máxima seguridad de la **notarización en Blockchain** o si es suficiente con un archivado seguro y versionado.

Por favor, completen la siguiente tabla. Hemos añadido algunos ejemplos para guiar el proceso.

| Nombre del Documento | ¿Generado por qué Proceso? | Obligatoriedad Legal/Fiscal | **¿Requiere Inmutabilidad?** <br> *(Es decir, ¿necesita prueba matemática de que no ha sido alterado en el tiempo? -> **Blockchain**)* |
| :--- | :--- | :---: | :---: |
| **Ej: Factura de Venta** | Facturación | **Alta** | **Sí** |
| **Ej: Contrato de Servicio** | Gestión de Contratos | **Alta** | **Sí** |
| **Ej: Registro de Reserva** | Gestión de Reservas | Media | No (Suficiente con registro y hash) |
| **Ej: Orden de Compra** | Pagos a Proveedores | Media | No |
| **Ej: Cotización** | Ventas y Cotizaciones | Baja | No |
| | | | |
| *(Por favor, continúen listando todos sus documentos)* | | | |
| | | | |
| | | | |
| | | | |

---

## Cierre

La información recopilada en este documento es fundamental. Con ella, podremos configurar el Sistema de Gestión Archivística para que funcione como el notario digital central de todo el ERP, asegurando que cada documento importante esté exactamente donde debe estar, con el nivel de seguridad que su negocio requiere.

¡Muchas gracias por su colaboración!
