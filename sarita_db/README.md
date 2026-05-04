# SARITA ERP - Gestión Comercial Omnicanal (Fase 10.5)

## Arquitectura de Crecimiento Autónomo

Este módulo transforma la gestión comercial en un motor inteligente capaz de vender, publicar contenido y atender clientes sin intervención humana constante.

### Estructura de Submódulos

- `01_crm/`: Base de datos de clientes, leads, perfiles y canales de comunicación (WhatsApp, IG, etc).
- `02_ventas/`: Gestión de pedidos, cotizaciones, embudos de venta (funnels) y métricas de conversión omnicanal.
- `03_marketing/`: Campañas, canales publicitarios y vinculación directa con contenido multimedia.
- `04_fidelizacion/`: Programas de lealtad y retención de clientes.
- `05_contenido_multimedia/`: Motor de creación de video, gestión de assets, timelines de edición y renders.
- `06_social_media/`: Integración con plataformas sociales, programación de posts, metrics y mensajería unificada.
- `07_automatizacion_comercial/`: Reglas de negocio automáticas, disparadores y acciones de respuesta inmediata.
- `08_ia_conversacional/`: Sesiones de chat inteligentes, registro de intenciones y ejecución de acciones comerciales autónomas.

## Reglas de Oro del Motor Comercial

1. **Omnicanalidad Real**: Cada interacción (mensaje, comentario, lead) se rastrea desde su origen hasta la conversión final.
2. **Metadata-First**: El contenido multimedia se gestiona mediante metadata y rutas, nunca almacenando binarios directamente en la DB.
3. **Conversión IA**: Los agentes de IA tienen la capacidad de proponer y ejecutar ventas, notificando al sistema mediante el bus de eventos.
4. **Seguridad Multi-inquilino**: Aislamiento estricto por `tenant_id` y acceso granular por roles empresariales.
