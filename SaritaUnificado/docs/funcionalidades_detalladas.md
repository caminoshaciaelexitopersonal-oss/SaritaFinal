0. Convenciones generales

API prefix: /api/v1/

Autenticación: JWT Bearer (Authorization: Bearer <token>)

Multitenancy: object-level permission by dependencia_id (cada entidad solo accede a su scope)

Auditar: todo cambio crítico debe tener AuditLog (user_id, action, resource_type, resource_id, timestamp, before, after)

1. Funcionalidades de cara al cliente (cliente final / portal público)

Objetivo: permitir a cualquier usuario descubrir información pública.

1.1 Buscador de destinos y prestadores

Autocomplete por nombre/municipio/tipo.

Filtros: tipo (hotel, restaurante, guía), ubicación (departamento, municipio), rango de precios, calificación, disponibilidad por fecha.

Endpoint: GET /api/v1/busqueda/?q=&tipo=&departamento=&municipio=&desde=&hasta=&page=

1.2 Ficha pública de recurso (atractivo/empresa/evento)

Muestra: nombre, galería imágenes, descripción, geo (lat/lng), horarios, contactos, RNT (si público), tags, reviews, calendario de disponibilidad.

Endpoint: GET /api/v1/atractivos/{slug}/ y GET /api/v1/empresas/{slug}/

1.3 Mapas y rutas

API devuelve GeoJSON; integración frontend con Leaflet/Mapbox.

Endpoint: GET /api/v1/mapa/atractivos/?bbox=...

1.4 Reservas públicas (turista)

Checkout simplificado: reservar producto/servicio → notificación al prestador + crear Reserva en estado pendiente.

Endpoint: POST /api/v1/reservas/ (payload detallado en plantilla)

1.5 Autenticación turista (opcional con social login)

Registro rápido con email, teléfono; verificación por email/SMS; persistencia de perfil y reservas.

2. Funcionalidades de cara al TURISTA (usuario autenticado)

2.1 Perfil del turista

historial reservas, tickets, favoritos, valoraciones, documentos (si aplica).
2.2 Reservas y pagos

crear, ver, cancelar reservas; ver estado y comunicación con prestador.

Integraciones de pago (pago externo o instructivo) — guardar payment_reference.
2.3 Feedback y reviews

rating 1–5, comentario; moderación por Admin Dependencia.
2.4 Chatbot asistente (interacción con Coronel local)

flujo natural con contexto de sesión; sugerencias automáticas (sitios cercanos).

3. Funcionalidades de cara al FUNCIONARIO DIRECCIÓN

Rol: coordinación y gestión estratégica por dependencia.

3.1 Dashboard Dirección

KPIs: ocupación por municipio, número prestadores activos, alertas RNT vencidas, incidentes SG-SST.

Widgets configurables (periodo, dependencia).

3.2 Gestión de atractivos y rutas

CRUD atractivos turísticos y rutas asociadas (multi-valued: puntos, etapas).

Validación por dependencia (workflow: borrador → revisión → publicado).

3.3 Gestión de eventos y promoción

Crear campañas/patrocinios; integrarse con panel prestadores para mostrar promociones.

3.4 Reportes y exportes

Export CSV/PDF por filtros (fechas, municipios).

3.5 Supervisión del Coronel y agentes

Panel IA: ver logs de interacciones, re-asignar coronel, establecer políticas de escalamiento (ej.: escalamiento a Sarita departamento).

3.6 Aprobación documental

Validar documentos subidos por prestadores (RNT, licencias) y registrar decisiones.

4. Funcionalidades de cara al FUNCIONARIO PROFESIONAL

Rol: ejecución técnica y supervisión operativa.

4.1 Gestión operativa diaria

Asignación de tareas, seguimiento de proyectos, control de calidad de registros (inspecciones).

4.2 Sistema de inspección y visitas de campo

Crear Programación de visitas, checklists (SG-SST, cumplimiento), subir evidencia (fotos), generar informe.

4.3 Soporte a prestadores

Generar capacitaciones, talleres; seguimiento de asistencia y certificación.

4.4 Acceso a datos y analítica

Visualizaciones técnicas de datasets: flujos turísticos, origen visitantes, tendencias.

5. Funcionalidades de cara al FUNCIONARIO TÉCNICO

Rol: operativo en campo y soporte técnico.

5.1 Tareas y órdenes de trabajo

Recibir tareas asignadas por profesionales o coroneles, marcar estado, subir evidencia.

5.2 Recolección de datos en campo

Formularios offline (si PWA) para levantar información básica y sincronizar cuando haya conexión.

5.3 Gestión documental y mantenimiento de recursos

Reportar incidencias, mantenimiento de activos, control de inventarios simples.

6. Funcionalidades para PRESTADORES (panel económico / comercial)

El panel del prestador es el motor comercial. Debe contener funcionalidades completas y separadas por tipo de prestador. Incluye:

6.1 Panel general del Prestador (dashboard)

KPIs: reservas pendientes, ocupación % por periodo, ingresos estimados, documentos por validar.

Alertas legales: RNT próximo a vencerse, documentos pendientes.

6.2 Perfil de empresa

Campos obligatorios: nombre, tipo (hotel, restaurante, guia,...), slug, dirección, municipio_id, departamento_id, tel, email, propietario_id, rnt, estado_rnt (pendiente/validado/rechazado), geo.

Validaciones: RNT formato, teléfono E.164, slug único por municipio.

6.3 Gestión de Documentos (RNT, licencias)

Subida con metadatos: tipo documento, fecha emisión, fecha expiración, archivo, estado validación.

Notificaciones automáticas a Admin Dependencia para revisión.

6.4 Catálogo de Productos/Servicios

Crear productos: tipo (habitacion, tour, menu, servicio transporte), descripción, atributos (capacidad, duración), fotos.

Tarifas: precio base + reglas temporales (temporada alta/baja), descuentos por cupo.

Recursos vinculados: habitaciones (nº), vehículos (placa/id), mesas (nº).

6.5 Calendario y disponibilidad

Calendario por producto y por recurso; bloqueos manuales; sincronización con OTA vía webhooks.

6.6 Reservas y gestión de pedidos

Vista lista, filtros por estado (pendiente, confirmado, cancelado, completado).

Acciones: confirmar, cancelar, reprogramar, emitir factura simplificada.

Mensajería con cliente (historial por reserva).

6.7 Gestión de usuarios internos (empleados)

Crear usuarios asociados a la empresa con roles internos: manager, operaciones, contador.

Permisos granulares (ej.: manager puede CRUD productos; operaciones puede gestionar reservas).

6.8 Inventario y recursos

Registrar activos (habitaciones/vehículos/equipos) con historial de movimientos.

Movimientos: asignación, mantenimiento, baja.

6.9 Finanzas y facturación (básico)

Registro de transacciones, facturas sencillas, reportes de ingresos por periodo.

Integración opcional con contabilidad municipal/export contable.

6.10 Reportes y exportes

Ocupación por periodo, top productos, ingresos por fuente (local/extranjero), cancelaciones.

6.11 Integración de agentes (Coronel local)

El Coronel puede enviar notificaciones automáticas (reserva nueva, documento vencido), responder FAQs y generar reportes automáticos para el prestador.

7. Sistema de Gestión Corporativa (Panel administrativo del servidor turístico)

Este panel es central para Administrador General y Administrador de Dependencia. Contiene:

7.1 Talento Humano

Modelos: Cargo, Empleado (user FK, cargo FK, dependencia), Capacitacion, Contrato.

Funcionalidades: gestión de plantilla, asignación de cargos, solicitud de vacaciones, historial formativo.

7.2 SG-SST (Salud y Seguridad en el Trabajo)

Matriz de riesgos por dependencia/actividad.

Incidentes: registro, evidencia, acciones correctivas.

Planes de prevención y actividades programadas.

Alertas de cumplimiento y reportes descargables.

7.3 Contabilidad (módulo simplificado)

Cuentas, transacciones, registro de ingresos por servicios, reportes (ingresos/gastos).

Interfaces para exportar a software contable municipal.

Gestión de comprobantes y conciliación simple.

7.4 Nómina

Registro de nómina: empleados, periodos de pago, conceptos, pagos (marcados como pagados)

Export CSV para nómina y pagos (con campos banco, tipo de documento).

7.5 Gestión Documental

Repositorio con versionado: subir, validar, expiración, notificaciones automáticas.

7.6 Planeación y Proyectos

Crear proyectos, fases, responsables, hitos, presupuesto asignado y seguimiento.

7.7 Auditoría & Compliance

Registro inmutable de acciones críticas (auditable por Admin General).

Export histórico por usuario/fecha/acción.

8. Registro y ubicación de entidades, empresas y usuarios (proceso detallado)
8.1 Inscripción de Entidades Municipales y Departamentales

Entidad municipal: registro por Admin General o Admin Dependencia con campos:

tipo_entidad = 'municipal'

nombre_oficial (ej. "Dirección de Turismo de Puerto Gaitán")

departamento_id, municipio_id (codificado según DANE)

slug, codigo_interno, contacto (email, tel), direccion_legal

Entidad departamental: similar pero tipo_entidad = 'departamental' y jurisdiccion = lista municipios.

Validaciones: verificación de datos DANE, verificación por Admin General (workflow: solicitado → verificado → activado).

8.2 Ubicación / Linkeo en el territorio

Todas las entidades y empresas guardan departamento_id y municipio_id (referencia a tabla geo_municipios con código DANE).

Geo exacto: lat, lng para mapas.

Relaciones: Empresa.dependencia_id (si la empresa está adscrita a una dependencia para seguimiento) — opcional.

8.3 Registro de Empresas y Personas (prestadores/artesanos)

Empresa (prestador):

Formulario: razon_social, nombre_comercial, tipo_empresa, rnt, nit (si aplica), direccion, municipio_id, lat/lng, propietario_user_id, contacto.

Flujo: crear → subir documentos → estado pendiente → revisión por Admin Dependencia → validado o rechazado.

Slug generado automáticamente slugify(nombre_comercial + municipio).

Persona natural (guía/artesano):

nombres, apellidos, documento_tipo, documento_num, telefono, correo, municipio, perfil (habilidades), certificados.

Validación por dependencia si requiere formalización.

8.4 Registro de Turistas

Registro simple: nombre, email, telefono (opcional), pais_origen, documento (opcional).

Si turista = extranjero → pais_origen obligatorio; sistema recomienda contenidos en su idioma.

9. Reglas de datos, validaciones y protección

Campos obligatorios por rol y tipo (lista en CODEBOOK).

Enmascaramiento de claves (aplicar mask en respuestas API).

GDPR/Colombia: consentimiento y eliminación de datos personales (endpoint para solicitar borrado).

Logs de auditoría para acceso a datos personales.

10. Endpoints de ejemplo y payloads (ejemplo práctico)

Crear empresa (prestador)
POST /api/v1/prestadores/empresas/
Payload:

{
  "nombre_comercial": "Hotel Sol y Luna",
  "razon_social":"Sol y Luna S.A.S",
  "tipo":"hotel",
  "municipio_id": 25001,
  "departamento_id": 25,
  "direccion": "Cra 10 # 20-30",
  "tel":"+573001234567",
  "email":"contacto@solyluna.com",
  "rnt":"RNT-2025-0001"
}


Respuesta esperada 201 con id, slug, estado_rnt: "pendiente".

Subir documento RNT
POST /api/v1/prestadores/empresas/{id}/documentos/ — multipart form-data: tipo_documento, archivo, fecha_emision, fecha_expiracion.

11. Pruebas y criterios de aceptación (por módulo)

Tests unitarios: modelos, serializers y permisos.

Tests integración: endpoints clave (registro empresa, subir doc, crear producto, reservar).

E2E: flujo prestador completo + flujo turista reserva + verificación por Admin Dependencia.

Cobertura objetivo >= 85% en módulos críticos.

12. Entregables esperados del informe de Jules (recap)

Documento completo rellenando la Plantilla (A).

Capturas / vídeos de flujos críticos.

Lista de endpoints con curl de ejemplo.

Migraciones aplicadas y changelog.

Lista de pendientes y roadmap corto.