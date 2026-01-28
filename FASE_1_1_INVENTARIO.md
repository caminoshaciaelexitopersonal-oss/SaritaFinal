# INFORME DE INVENTARIO - FASE 1.1 (ACTUALIZADO)

## 1.1.A — Análisis de `backend/apps/sadi_agent`

... (Esta sección no ha cambiado) ...

## 1.1.B — Análisis de `backend/apps/sarita_agents` (POST-MIGRACIÓN)

### 1. Jerarquía Real Existente (Detallada)

Tras la migración, la jerarquía en `sarita_agents` representa la totalidad de la lógica de negocio. A continuación se detalla cada Capitán:

-   **General (1):**
    -   `sarita` (Orquestador principal)
-   **Coroneles (4):**
    -   `administrador_general`
    -   `clientes_turistas`
    -   `gubernamental`
    -   `prestadores`

---

### **Desglose de Capitanes por Coronel:**

#### **Coronel: `administrador_general`**
-   `capitanes/capitan_auditoria_global.py`
-   `capitanes/capitan_configuracion_sistema.py`
-   `capitanes/capitan_gobernanza_agentes.py`
-   `capitanes/capitan_monitoreo_plataforma.py`
-   `capitanes/capitan_seguridad_accesos.py`

#### **Coronel: `clientes_turistas`**
-   `capitanes/capitan_busqueda_servicios.py`
-   `capitanes/capitan_contexto_viaje.py`
-   `capitanes/capitan_experiencia_turista.py`
-   `capitanes/capitan_gestion_perfil.py`
-   `capitanes/capitan_pqrs.py`
-   `capitanes/capitan_reservas_turista.py`

#### **Coronel: `gubernamental`**
-   **Sub-dominio: `departamental`**
    -   `capitanes/capitan_coordinacion_municipal.py`
    -   `capitanes/capitan_planificacion_regional.py`
    -   `capitanes/capitan_rutas_turisticas.py`
-   **Sub-dominio: `municipal`**
    -   `capitanes/capitan_control_prestadores.py`
    -   `capitanes/capitan_eventos_locales.py`
    -   `capitanes/capitan_turismo_local.py`
-   **Sub-dominio: `nacional`**
    -   `capitanes/capitan_estandares_certificaciones.py`
    -   `capitanes/capitan_indicadores_nacionales.py`
    -   `capitanes/capitan_politicas_nacionales.py`

#### **Coronel: `prestadores`**
-   **Sub-dominio: `gestion_archivistica`**
    -   `capitanes/capitan_base.py`
    -   `capitanes/capitan_busqueda_documental.py`
    -   `capitanes/capitan_captura_y_creacion_documental.py`
    -   `capitanes/capitan_cumplimiento_normativo.py`
    -   `capitanes/capitan_digitalizacion_documental.py`
    -   `capitanes/capitan_gestion_archivistica_general.py`
    -   `capitanes/capitan_seguridad_documental.py`
    -   `capitanes/capitan_trazabilidad_documental.py`
-   **Sub-dominio: `gestion_comercial`**
    -   `capitanes/capitan_base.py`
    -   `capitanes/capitan_embudos_conversion.py`
    -   `capitanes/capitan_gestion_comercial_general.py`
    -   `capitanes/capitan_gestion_operativa_de_contenidos_comerciales.py`
    -   `capitanes/capitan_implementacion_tecnica_de_embudos_y_crm.py`
    -   `capitanes/capitan_inteligencia_analitica_y_optimizacion.py`
    -   `capitanes/capitan_marketing.py`
    -   `capitanes/capitan_mensajeria_y_envios_masivos.py`
    -   `capitanes/capitan_produccion_y_automatizacion_audiovisual.py`
    -   `capitanes/capitan_publicidad_y_adquisicion_de_trafico_ads.py`
    -   `capitanes/capitan_relacion_clientes.py`
    -   `capitanes/capitan_ventas.py`
-   **Sub-dominio: `gestion_contable`**
    -   `activos_fijos/capitan_adquisiciones_y_compras.py`
    -   `activos_fijos/capitan_bajas_y_disposicion_final.py`
    -   ... (y muchos más)
-   **Sub-dominio: `gestion_financiera`**
    -   ... (y muchos más)
-   **Sub-dominio: `gestion_operativa`**
    -   ... (y muchos más)

... (El resto del archivo permanece sin cambios) ...
