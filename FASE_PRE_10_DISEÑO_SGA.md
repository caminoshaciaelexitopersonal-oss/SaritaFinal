# FASE PRE-10: Diseño Técnico-Funcional del Sistema de Gestión Archivística (SGA)

---

## 1. Resumen Ejecutivo

Este documento consolida el diseño completo para la integración del Sistema de Gestión Archivística (SGA) como un módulo transversal y notarial dentro del ERP "Sarita". El objetivo del SGA es garantizar la integridad, inmutabilidad y trazabilidad de todos los documentos críticos generados por los módulos de negocio.

La fase PRE-10 ha consistido en un análisis profundo para mapear los puntos de integración, definir una estrategia de archivado específica para cada documento y diseñar una API interna robusta y desacoplada. Este documento presenta los resultados de dicha fase y sirve como el plan maestro para la implementación técnica.

---

## 2. Anexo A: Propuesta de Levantamiento de Requisitos

Para asegurar que el SGA se alinee con las necesidades del negocio, se ha preparado el siguiente documento guía para una sesión de trabajo con el cliente. Su propósito es definir la taxonomía (clasificación) y los niveles de criticidad de los documentos que el sistema gestionará.

```markdown
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
```

---

## 3. Arquitectura y Diseño Técnico

### 3.1. Puntos de Integración Identificados

El análisis del código fuente ha revelado los siguientes puntos de anclaje ideales para disparar el proceso de archivado. Estos puntos garantizan que los documentos se capturen en su estado final y más completo.

*   **Módulo `gestion_comercial`**:
    *   **Punto Exacto:** Dentro del servicio `FacturacionService`, en el método `facturar_operacion_confirmada`.
    *   **Momento:** Inmediatamente después de recibir y guardar la respuesta de la DIAN para una `FacturaVenta`.

*   **Módulo `gestion_contable`**:
    *   **Punto Exacto:** Dentro del servicio `FacturaVentaAccountingService`, en el método `registrar_factura_venta`.
    *   **Momento:** Justo después de que la validación `clean()` del `JournalEntry` (Asiento Contable) sea exitosa.

*   **Módulo `gestion_financiera`**:
    *   **Punto Exacto:** Dentro del servicio `PagoService`, en el método `crear_orden_pago_empleado`.
    *   **Momento:** En el instante en que se crea una `OrdenPago` con el estado `PAGADA`.

*   **Módulo `gestion_operativa`**:
    *   **Punto Exacto:** Dentro del `ReservaViewSet`, en el método `perform_create`.
    *   **Momento:** Inmediatamente después de la llamada `serializer.save()` que persiste la `Reserva` en la base de datos.

### 3.2. Estrategia de Archivado por Documento

Basado en el análisis, se propone la siguiente estrategia técnica para cada documento clave.

```markdown
# Estrategia de Integración del Sistema de Gestión Archivística (SGA)

Este documento detalla la estrategia de archivado para cada tipo de documento clave identificado en los módulos de negocio del ERP "Sarita".

---

## 1. Documento: Factura de Venta (`FacturaVenta`)

-   **Módulo de Origen:** `gestion_comercial`
-   **Punto de Disparo:** `FacturacionService.facturar_operacion_confirmada()`
-   **Descripción:** Documento fiscal y legal que representa una venta completada y aceptada por la DIAN. Su integridad es de máxima criticidad.

### Estrategia de Archivado:

-   **¿Qué datos se archivarán?**
    -   **Formato Primario:** `PDF`. Se deberá generar una representación visual estandarizada de la factura, incluyendo el CUFE y otros detalles fiscales.
    -   **Metadatos:** El `JSON` con los datos del modelo `FacturaVenta` se almacenará como metadato para búsquedas y análisis.

-   **¿Cuándo se archivará?**
    -   **Mecanismo:** En **tiempo real**. La llamada al servicio de archivado se realizará inmediatamente después de que la factura se guarde con el estado final de la DIAN.

-   **¿Qué nivel de seguridad necesita?**
    -   **Nivel:** **Máximo - Notarización Blockchain**.
    -   **Proceso:** El hash SHA-256 del archivo PDF se calculará y se anclará en la blockchain a través del proceso de notarización del SGA (árboles de Merkle).

-   **¿Cómo se clasifica en el SGA?**
    -   **ProcessType Code:** `CONT` (Contabilidad)
    -   **Process Code:** `FACT` (Facturación)
    -   **DocumentType Code:** `FV` (Factura de Venta)

---

## 2. Documento: Asiento Contable (`JournalEntry`)

-   **Módulo de Origen:** `gestion_contable`
-   **Punto de Disparo:** `FacturaVentaAccountingService.registrar_factura_venta()`
-   **Descripción:** Registro fundamental que refleja el impacto de una transacción en el libro mayor. Es la "verdad contable" y su inmutabilidad es crítica para la confianza financiera.

### Estrategia de Archivado:

-   **¿Qué datos se archivarán?**
    -   **Formato Primario:** `JSON`. Se serializará el objeto `JournalEntry` junto con sus `Transaction` hijas a un formato JSON canónico. Este formato es ideal para auditorías automatizadas.

-   **¿Cuándo se archivará?**
    -   **Mecanismo:** En **tiempo real**. Inmediatamente después de que el `JournalEntry` pase la validación del método `clean()`.

-   **¿Qué nivel de seguridad necesita?**
    -   **Nivel:** **Máximo - Notarización Blockchain**.
    -   **Proceso:** El hash SHA-256 del string JSON canónico será enviado para notarización en la blockchain.

-   **¿Cómo se clasifica en el SGA?**
    -   **ProcessType Code:** `CONT` (Contabilidad)
    -   **Process Code:** `CONT-GEN` (Contabilidad General)
    -   **DocumentType Code:** `AC` (Asiento Contable)

---

## 3. Documento: Orden de Pago (`OrdenPago`)

-   **Módulo de Origen:** `gestion_financiera`
-   **Punto de Disparo:** `PagoService.crear_orden_pago_empleado()`
-   **Descripción:** Documento que evidencia una salida de dinero de la empresa (egreso). Crucial para el control de tesorería y auditorías.

### Estrategia de Archivado:

-   **¿Qué datos se archivarán?**
    -   **Formato Primario:** `PDF`. Se generará un comprobante de egreso o recibo de pago en formato PDF.

-   **¿Cuándo se archivará?**
    -   **Mecanismo:** En **tiempo real**, en el momento en que la orden de pago se crea con el estado `PAGADA`.

-   **¿Qué nivel de seguridad necesita?**
    -   **Nivel:** **Alto - Notarización Blockchain**.
    -   **Proceso:** El hash del PDF será anclado en la blockchain.

-   **¿Cómo se clasifica en el SGA?**
    -   **ProcessType Code:** `FIN` (Finanzas)
    -   **Process Code:** `PAGOS` (Pagos y Egresos)
    -   **DocumentType Code:** `OP` (Orden de Pago)

---

## 4. Documento: Registro de Reserva (`Reserva`)

-   **Módulo de Origen:** `gestion_operativa`
-   **Punto de Disparo:** `ReservaViewSet.perform_create()`
-   **Descripción:** Registro operativo que confirma un acuerdo de servicio con un cliente. Su integridad es importante para la gestión, pero de menor criticidad fiscal.

### Estrategia de Archivado:

-   **¿Qué datos se archivarán?**
    -   **Formato Primario:** `JSON`. Se serializarán los datos del modelo `Reserva` a JSON, capturando el estado de la reserva en el momento de su creación.

-   **¿Cuándo se archivará?**
    -   **Mecanismo:** En **tiempo real**, inmediatamente después de que la reserva se guarde en la base de datos.

-   **¿Qué nivel de seguridad necesita?**
    -   **Nivel:** **Medio - Hash simple (SHA-256)**.
    -   **Proceso:** El hash del JSON se calculará y se almacenará en el campo `file_hash_sha256` del `DocumentVersion`. No se enviará para notarización en blockchain, dejando los campos `merkle_root` y `blockchain_transaction` nulos. Esto permite una verificación de integridad interna sin incurrir en costos de transacción de blockchain.

-   **¿Cómo se clasifica en el SGA?**
    -   **ProcessType Code:** `OPER` (Operaciones)
    -   **Process Code:** `RESERV` (Gestión de Reservas)
    -   **DocumentType Code:** `RES-REG` (Registro de Reserva)
```

### 3.3. Diseño de la API Interna (`ArchivingService`)

Para implementar la estrategia de forma limpia y desacoplada, se ha diseñado un servicio centralizado, `ArchivingService`, que actuará como la única puerta de entrada al SGA para el resto de los módulos.

Este enfoque de **Fachada (Facade)** simplifica enormemente la integración, ya que los módulos de negocio no necesitan conocer los detalles internos del versionado, cálculo de hashes, almacenamiento en S3 o la comunicación con la blockchain.

La firma de la API propuesta es la siguiente:

```python
# backend/apps/prestadores/mi_negocio/gestion_archivistica/services.py

from django.db import models
from django.contrib.auth import get_user_model
from typing import Dict, Any, Union
import io

# ... (imports y placeholders) ...

class ArchivingService:
    """
    Punto de entrada centralizado para todas las operaciones de archivado.
    Esta clase orquesta la creación de documentos, versiones y la
    gestión de su ciclo de vida.
    """

    @staticmethod
    def archive_document(
        *,
        perfil_prestador_id: int,
        user_id: int,
        process_type_code: str,
        process_code: str,
        document_type_code: str,
        document_content: Union[bytes, io.BytesIO],
        original_filename: str,
        document_metadata: Dict[str, Any],
        requires_blockchain_notarization: bool = False
    ) -> 'DocumentVersion':
        """
        Método principal para archivar un nuevo documento o una nueva versión
        de un documento existente.

        Args:
            perfil_prestador_id (int): ID del Perfil del Prestador (Tenant).
            user_id (int): ID del usuario que realiza la acción.
            process_type_code (str): Código del Tipo de Proceso (e.g., 'CONT').
            process_code (str): Código del Proceso específico (e.g., 'FACT').
            document_type_code (str): Código del Tipo de Documento (e.g., 'FV').
            document_content (Union[bytes, io.BytesIO]): Contenido binario del
                                                        archivo a archivar (e.g., PDF, JSON).
            original_filename (str): Nombre del archivo original con extensión (e.g., 'factura-001.pdf').
            document_metadata (Dict[str, Any]): JSON con metadatos relevantes
                                               del documento original para indexación y búsqueda.
            requires_blockchain_notarization (bool): Si es True, el hash del
                                                     documento será incluido en el
                                                     siguiente lote de notarización.

        Returns:
            DocumentVersion: La instancia de la versión del documento creada.

        Raises:
            ValidationError: Si los códigos de clasificación no existen o los
                             parámetros son inválidos.
        """
        # --- IMPLEMENTACIÓN FUTURA ---
        pass

    # ... (otros métodos auxiliares como get_document_status, retrieve_document) ...
```

---

## 4. Próximos Pasos

Con la aprobación de este documento de diseño, la siguiente fase (FASE-10) consistirá en la **implementación técnica** de los puntos aquí definidos:
1.  Desarrollar la lógica interna del `ArchivingService`.
2.  Implementar la generación de los archivos (PDF y JSON) en cada módulo de negocio.
3.  Insertar las llamadas al `ArchivingService` en los puntos de integración identificados.
4.  Crear las pruebas unitarias y de integración para validar el flujo completo de archivado.
