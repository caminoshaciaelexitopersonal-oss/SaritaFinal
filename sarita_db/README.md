# SARITA ERP - Gestión Archivística Institucional (Fase 10.7)

## Sistema de Verdad Legal y Custodia Inmutable

Este módulo implementa la infraestructura para la gestión formal de documentos, expedientes y evidencias legales bajo estándares gubernamentales y forenses.

### Estructura de Submódulos

- `01_estructura_documental/`: Definición jerárquica de tipos y categorías.
- `02_expedientes/`: Gestión de carpetas raíz (Files) vinculadas a procesos o entidades.
- `03_documentos/`: Entidades de documento principal con vinculación a expedientes.
- `04_versionado/`: Control inmutable de versiones (no sobrescritura).
- `05_metadatos/`: Esquemas dinámicos para indexación técnica.
- `06_clasificacion/`: Reglas para clasificación automática mediante IA.
- `07_ciclo_vida/`: Máquina de estados (Creado -> Firmado -> Archivado).
- `08_accesos_seguridad/`: Logs forenses de acceso y permisos granulares.
- `09_firma_electronica/`: Orquestación de firmas múltiples.
- `10_notarizacion/`: Integración con servicios de fe pública (Blockchain-ready).
- `11_ocr_extraccion/`: Digitalización y extracción de texto de imágenes.
- `12_trazabilidad/`: Registro detallado de eventos archivísticos.
- `13_retencion_disposicion/`: Políticas legales de conservación y purga.
- `14_exportacion_auditoria/`: Generación de paquetes para entes de control.

## Reglas de Oro Archivísticas

1. **Inmutabilidad**: Las versiones de documentos nunca se actualizan; se crean nuevas filas con hash SHA256 obligatorio.
2. **Metadata-Only**: La DB solo almacena la metadata y el hash; los archivos físicos residen en storage externo auditado.
3. **Firma Obligatoria**: Los documentos legales requieren una solicitud de firma vinculada a la versión específica.
4. **Trazabilidad Forense**: Cada visualización o descarga se registra con IP y timestamp en `access_logs`.
