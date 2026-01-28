# Análisis de Brechas: Módulo de Gestión Archivística

**Fecha de Análisis:** 2025-11-08
**Auditor:** Jules

## 1. Resumen Ejecutivo

El módulo de `gestion_archivistica` en Sarita tiene una base sólida a nivel de modelos de datos y una API funcional para operaciones CRUD básicas. Sin embargo, al compararlo con la arquitectura de referencia de "DocFlow", se identifican **brechas significativas** en áreas críticas como la seguridad (cifrado), el rendimiento (procesamiento asíncrono), la extensibilidad (abstracción de almacenamiento) y la fiabilidad (pruebas y CI/CD).

La implementación actual es **síncrona y no segura**, lo que significa que los archivos se manejan en texto plano y bloquean el servidor durante la subida. La funcionalidad de blockchain está presente en los modelos, pero no hay lógica de backend para implementarla. El frontend consiste en una tabla de datos básica con un formulario de subida, pero carece de funcionalidades avanzadas.

Este documento detalla las funcionalidades existentes y las que faltan para elevar el módulo al nivel de robustez de "DocFlow".

---

## 2. Funcionalidades Existentes en Sarita

### 2.1. Backend

*   **Modelos de Datos:**
    *   `ProcessType`, `Process`, `DocumentType`: Modelos de catálogos para clasificar documentos.
    *   `Document`: Contenedor lógico para un documento y sus versiones.
    *   `DocumentVersion`: Modelo bien definido que incluye un ciclo de vida (`status`), campos para el hash y el ID de almacenamiento externo, y placeholders para la prueba de blockchain (`merkle_root`, `blockchain_transaction`, etc.).
*   **API (Endpoints):**
    *   Endpoints CRUD básicos para `Document` y `DocumentVersion` a través de un `ViewSet`.
    *   Endpoints de solo lectura para los catálogos.
    *   La API gestiona correctamente la multi-tenencia (un usuario solo ve los documentos de su compañía).
*   **Lógica de Negocio:**
    *   Existe un `DocumentCoordinatorService` que es llamado desde la vista.
    *   **Importante:** Toda la lógica de negocio (lectura de archivo, creación de modelos) se ejecuta **de forma síncrona** dentro de la petición HTTP.

### 2.2. Frontend

*   **Estructura de Archivos:** Existe una página principal (`page.tsx`), una vista de detalle (`[documentId]`) y una carpeta de componentes.
*   **Funcionalidad Principal:**
    *   Una tabla de datos (`DataTable`) que utiliza `@tanstack/react-query` para obtener y mostrar la lista de documentos desde la API.
    *   La tabla muestra un esqueleto de carga (`DataTableSkeleton`) mientras se obtienen los datos.
    *   Un diálogo modal (`UploadDialog`) que permite (teóricamente) subir un nuevo documento.

---

## 3. Brechas Identificadas (Funcionalidades Faltantes vs. DocFlow)

### 3.1. Brecha Crítica: Seguridad y Rendimiento (Backend)

*   **Cifrado de Conocimiento Cero (Zero-Knowledge):**
    *   **Falta:** No existe un sistema de cifrado. Los archivos se reciben y (se asumiría) se almacenan en texto plano.
    *   **Requerido (DocFlow):** Implementación de `CryptoService` y `KeyDerivationService` para cifrar cada archivo con una clave única y determinista por compañía antes de almacenarlo.
*   **Procesamiento Asíncrono con Celery:**
    *   **Falta:** El `DocumentCoordinatorService` actual lo hace todo de forma síncrona, bloqueando la petición del usuario y siendo propenso a timeouts con archivos grandes.
    *   **Requerido (DocFlow):** Refactorizar el `DocumentCoordinatorService` para que su única función sea iniciar una cadena de tareas de Celery (`file_processing_chain`). El trabajo pesado (hashear, cifrar, subir) debe ocurrir en segundo plano.
*   **Pipeline de Procesamiento de Archivos:**
    *   **Falta:** No hay un pipeline definido.
    *   **Requerido (DocFlow):** Implementar las tareas de Celery (`hash_and_upload_task`, `prepare_for_notarization_task`) que componen un flujo de trabajo resiliente y con reintentos.

### 3.2. Brecha Arquitectónica: Extensibilidad (Backend)

*   **Capa de Abstracción de Almacenamiento:**
    *   **Falta:** No hay una capa de abstracción. El sistema no tiene idea de dónde o cómo se almacenarán los archivos.
    *   **Requerido (DocFlow):** Introducir una interfaz `BaseStorageAdapter` y adaptadores concretos (`S3StorageAdapter`, `GoogleDriveStorageAdapter`, etc.). Esto permite cambiar de proveedor de almacenamiento en la nube sin alterar la lógica de negocio.
*   **Auditoría Detallada:**
    *   **Falta:** El sistema actual no registra eventos de gestión documental en un `AuditLog`.
    *   **Requerido (DocFlow):** Integrar con el `AuditLogger` para registrar cada acción (subida, descarga, verificación) de forma centralizada y segura.

### 3.3. Brecha Funcional: Blockchain (Backend)

*   **Notarización en Lote:**
    *   **Falta:** Los campos del modelo existen, pero no hay lógica que los llene.
    *   **Requerido (DocFlow):** Implementar la tarea periódica de Celery (`notarize_pending_documents_batch`) que agrupa los hashes, construye el Árbol de Merkle y ancla la raíz en un contrato inteligente de Polygon.

### 3.4. Brecha de Calidad: Pruebas y DevOps

*   **Pruebas de Integración:**
    *   **Falta:** No existen archivos de prueba para el módulo `gestion_archivistica`.
    *   **Requerido (DocFlow):** Crear una suite de pruebas (`test_api.py`, `test_services.py`) con `pytest` y `factory-boy` para asegurar la seguridad multi-tenencia, los permisos basados en roles y la correcta funcionalidad de la API.
*   **Pipeline de CI/CD:**
    *   **Falta:** No existe un archivo de workflow de GitHub Actions para el despliegue.
    *   **Requerido (DocFlow):** Implementar el `.github/workflows/deploy.yml` para automatizar la construcción de imágenes Docker, la ejecución de migraciones y el despliegue en AWS ECS para los entornos de `staging` y `main`.

### 3.5. Brecha Funcional: Interfaz de Usuario (Frontend)

*   **Visualización de Detalles:**
    *   **Falta:** La página de detalle (`[documentId]/page.tsx`) es probablemente un placeholder.
    *   **Requerido:** Una vista detallada que muestre todas las versiones de un documento, su estado actual (`VERIFIED`, `PENDING_CONFIRMATION`), el hash, y la información de la transacción de blockchain (con un enlace a PolygonScan).
*   **Descarga Segura:**
    *   **Falta:** No hay funcionalidad para descargar una versión específica de un documento.
    *   **Requerido:** Implementar la lógica para llamar al endpoint de descarga de la API, que a su vez debería obtener el archivo cifrado del almacenamiento, descifrarlo en el servidor y enviarlo de forma segura al cliente.
*   **Formulario de Subida Completo:**
    *   **Falta:** El `UploadDialog` actual es un simple botón.
    *   **Requerido:** Un formulario completo (usando `react-hook-form` y `zod`) para capturar todos los metadatos necesarios (`title`, `validity_year`, `process_id`, etc.) junto con el archivo.
