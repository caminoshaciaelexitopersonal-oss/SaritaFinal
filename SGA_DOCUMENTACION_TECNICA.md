# SGA: Documentación Técnica y Guía de Integración

---

## 1. Resumen Ejecutivo

Este documento describe la implementación técnica del Sistema de Gestión Archivística (SGA) y sirve como guía para integrar nuevos documentos en el futuro. El SGA funciona como un servicio notarial centralizado que garantiza la integridad y trazabilidad de los documentos críticos generados en el ERP.

---

## 2. Arquitectura y Diseño

### 2.1. Punto de Entrada Único: `ArchivingService`

La integración con el SGA se realiza **exclusivamente** a través del servicio `ArchivingService`, ubicado en `apps.prestadores.mi_negocio.gestion_archivistica.archiving`. Este servicio utiliza el patrón **Facade** para abstraer la complejidad del proceso de archivado.

### 2.2. API del Servicio

El método principal para archivar un documento es:

```python
ArchivingService.archive_document(
    *,
    company_id: int,
    user_id: int,
    process_type_code: str,
    process_code: str,
    document_type_code: str,
    document_content: Union[bytes, io.BytesIO],
    original_filename: str,
    document_metadata: Dict[str, Any],
    requires_blockchain_notarization: bool = False
) -> DocumentVersion
```

-   `company_id`, `user_id`: Identificadores del tenant y del usuario que realiza la acción.
-   `process_type_code`, `process_code`, `document_type_code`: Códigos de la taxonomía del SGA, que deben ser creados previamente en la base de datos (modelos `ProcessType`, `Process`, `DocumentType`).
-   `document_content`: Los bytes del archivo a archivar (ej. un JSON o un PDF).
-   `original_filename`: El nombre del archivo con su extensión.
-   `document_metadata`: Un diccionario que **debe** contener una clave `source_id` para vincular unívocamente el documento archivado con su origen (ej. `{'source_id': factura.id}`).
-   `requires_blockchain_notarization`: Booleano que indica si el hash del documento debe ser enviado a notarización (funcionalidad futura).

---

## 3. Guía de Integración: Ejemplo Piloto (`FacturaVenta`)

La integración de un nuevo documento sigue tres pasos:

### Paso 1: Modificar el Modelo de Origen

Añada una `ForeignKey` nulable al modelo `Document` del SGA en el modelo que origina el documento.

**Ejemplo en `FacturaVenta`:**
```python
# gestion_comercial/domain/models.py

class FacturaVenta(models.Model):
    # ... otros campos ...
    documento_archivistico = models.ForeignKey(
        'gestion_archivistica.Document',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='factura_comercial',
        help_text="Vínculo al registro maestro en el Sistema de Gestión Archivística."
    )
```
Después de añadir el campo, cree y aplique la migración correspondiente.

### Paso 2: Invocar el `ArchivingService`

En el punto de negocio donde el documento alcanza su estado final, invoque al `ArchivingService`.

**Ejemplo en `FacturacionService`:**
```python
# gestion_comercial/services.py
import json
from apps.prestadores.mi_negocio.gestion_archivistica.archiving import ArchivingService

class FacturacionService:
    @staticmethod
    @transaction.atomic
    def facturar_operacion_confirmada(operacion):
        # ... lógica de facturación ...
        factura = ...

        # --- INICIO DE INTEGRACIÓN CON SGA ---
        try:
            # Preparar contenido y metadatos
            factura_content = { "numero": factura.numero_factura, "total": str(factura.total) }
            factura_bytes = json.dumps(factura_content).encode('utf-8')
            metadata = {'source_id': factura.id}

            # Invocar al servicio
            document_version = ArchivingService.archive_document(
                company_id=factura.perfil.company.id,
                user_id=factura.creado_por.id,
                process_type_code='CONT',
                process_code='FACT',
                document_type_code='FV',
                document_content=factura_bytes,
                original_filename=f"{factura.numero_factura}.json",
                document_metadata=metadata,
                requires_blockchain_notarization=True
            )

            # Vincular el registro de archivo con la factura
            factura.documento_archivistico = document_version.document
            factura.save()

        except Exception as e:
            print(f"ERROR al archivar la factura: {e}")
        # --- FIN DE INTEGRACIÓN CON SGA ---

        # ... resto del servicio ...
        return factura
```

### Paso 3: Crear un Test de Integración

Añada un test al archivo `gestion_archivistica/tests/test_integration.py` para verificar que el nuevo flujo de negocio dispara el archivado correctamente.

**Ejemplo de verificación dentro del test:**
```python
# test_integration.py

# ... (setUp del test) ...

# Ejecutar el servicio de negocio
factura = FacturacionService.facturar_operacion_confirmada(operacion)

# Verificar que la factura está vinculada a un documento del SGA
self.assertIsNotNone(factura.documento_archivistico)
self.assertIsInstance(factura.documento_archivistico, Document)

# Verificar que se creó la versión del documento
self.assertEqual(factura.documento_archivistico.versions.count(), 1)
doc_version = factura.documento_archivistico.versions.first()

# Verificar el hash del contenido
factura_bytes = ... # Recrear el contenido exacto
expected_hash = hashlib.sha256(factura_bytes).hexdigest()
self.assertEqual(doc_version.file_hash_sha256, expected_hash)
```

---

## 4. Conclusión

Siguiendo estos tres pasos, cualquier módulo puede ser integrado con el SGA de una manera estandarizada, robusta y verificable, manteniendo el acoplamiento al mínimo y la lógica de archivo centralizada.
