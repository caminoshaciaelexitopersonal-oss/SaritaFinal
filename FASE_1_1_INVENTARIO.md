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
    -   `capitan_base.py`
    -   `capitan_busqueda_documental.py`
    -   `capitan_captura_y_creacion_documental.py`
    -   `capitan_cumplimiento_normativo.py`
    -   `capitan_digitalizacion_documental.py`
    -   `capitan_gestion_archivistica_general.py`
    -   `capitan_seguridad_documental.py`
    -   `capitan_trazabilidad_documental.py`
-   **Sub-dominio: `gestion_comercial`**
    -   `capitan_base.py`
    -   `capitan_embudos_conversion.py`
    -   `capitan_gestion_comercial_general.py`
    -   `capitan_gestion_operativa_de_contenidos_comerciales.py`
    -   `capitan_implementacion_tecnica_de_embudos_y_crm.py`
    -   `capitan_inteligencia_analitica_y_optimizacion.py`
    -   `capitan_marketing.py`
    -   `capitan_mensajeria_y_envios_masivos.py`
    -   `capitan_produccion_y_automatizacion_audiovisual.py`
    -   `capitan_publicidad_y_adquisicion_de_trafico_ads.py`
    -   `capitan_relacion_clientes.py`
    -   `capitan_ventas.py`
-   **Sub-dominio: `gestion_contable`**
    -   `capitan_activos_fijos_contabilidad.py`
    -   `capitan_auditoria_y_cumplimiento_niif.py`
    -   `capitan_base.py`
    -   `capitan_cierre_contable.py`
    -   `capitan_cierre_mensual_y_anual.py`
    -   `capitan_conciliaciones_bancarias.py`
    -   `capitan_consolidacion_financiera.py`
    -   `capitan_control_interno_contable.py`
    -   `capitan_cuentas_por_cobrar.py`
    -   `capitan_cuentas_por_pagar.py`
    -   `capitan_cumplimiento_contable.py`
    -   `capitan_estados_financieros.py`
    -   `capitan_eventos_auditoria.py`
    -   `capitan_gestion_contable_general.py`
    -   `capitan_impuestos.py`
    -   `capitan_inventarios_contabilidad.py`
    -   `capitan_nomina_contabilidad.py`
    -   `capitan_periodos_contables.py`
    -   `capitan_plan_de_cuentas_y_politicas.py`
    -   `capitan_presupuesto_y_control.py`
    -   `capitan_reportes_contables.py`
    -   `capitan_retenciones_y_otros_impuestos.py`
    -   `capitan_tesoreria_y_bancos.py`
    -   **`activos_fijos/`**
        -   `capitan_adquisiciones_y_compras.py`
        -   `capitan_bajas_y_disposicion_final.py`
        -   `capitan_depreciacion_contable.py`
        -   `capitan_depreciacion_fiscal.py`
        -   `capitan_inventario_fisico_y_trazabilidad.py`
        -   `capitan_mantenimiento_y_reparaciones.py`
        -   `capitan_revalorizacion_y_deterioro.py`
        -   `capitan_seguros_y_polizas.py`
        -   `capitan_transferencias_y_movimientos.py`
    -   **`nomina/`**
        -   `capitan_base.py`
        -   `capitan_control_y_pre_nomina.py`
        -   `capitan_cumplimiento_y_auditoria_nomina.py`
        -   `capitan_datos_maestros_empleados.py`
        -   `capitan_deducciones.py`
        -   `capitan_devengados_fijos.py`
        -   `capitan_devengados_variables.py`
        -   `capitan_liquidacion_contratos_y_retiros.py`
        -   `capitan_liquidacion_prestaciones_sociales.py`
        -   `capitan_liquidacion_seguridad_social_pila.py`
        -   `capitan_novedades_y_ausencias.py`
        -   `capitan_pagos_y_tesoreria.py`
        -   `capitan_parafiscales.py`
        -   `capitan_provisiones_y_consolidacion.py`
        -   `capitan_reportes_y_certificados.py`
-   **Sub-dominio: `gestion_financiera`**
    -   `capitan_analisis_financiero.py`
    -   `capitan_analisis_riesgo.py`
    -   `capitan_base.py`
    -   `capitan_contabilidad_y_estados_financieros.py`
    -   `capitan_control_financiero.py`
    -   `capitan_costos_y_rentabilidad.py`
    -   `capitan_flujo_caja.py`
    -   `capitan_gestion_financiera_general.py`
    -   `capitan_inversiones_y_mercado_capitales.py`
    -   `capitan_planificacion_financiera.py`
    -   `capitan_ratios_y_formulas_financieras.py`
    -   `capitan_riesgo_financiero.py`
-   **Sub-dominio: `gestion_operativa`**
    -   `capitan_base.py`
    -   `capitan_calidad_y_cumplimiento.py`
    -   `capitan_comunicaciones_operativas.py`
    -   `capitan_control_operativo.py`
    -   `capitan_gestion_operativa_general.py`
    -   `capitan_logistica_y_recursos.py`
    -   `capitan_operacion_alojamientos.py`
    -   `capitan_operacion_artesanos.py`
    -   `capitan_operacion_atracciones.py`
    -   `capitan_operacion_bares.py`
    -   `capitan_operacion_eventos.py`
    -   `capitan_operacion_experiencias.py`
    -   `capitan_operacion_gastronomia.py`
    -   `capitan_operacion_guias.py`
    -   `capitan_operacion_restaurantes.py`
    -   `capitan_operacion_tours.py`
    -   `capitan_operacion_transporte.py`
    -   `capitanes/capitan_operaciones_generales.py`
    -   `capitanes/capitan_orquestacion_por_voz.py`
    -   `capitanes/capitan_planificacion_servicios.py`
    -   `capitanes/capitan_reservas_y_agenda.py`
    -   **`sg_sst/`**
        -   `capitan_base.py`
        -   `capitan_cultura_y_participacion.py`
        -   `capitan_gestion_de_contratistas.py`
        -   `capitan_gestion_documental.py`
        -   `capitan_indicadores_y_analitica.py`
        -   `capitan_innovacion_y_tecnologia.py`
        -   `capitan_inspecciones_de_seguridad.py`
        -   `capitan_investigacion_de_incidentes.py`
        -   `capitan_matriz_de_peligros_iperc.py`
        -   `capitan_planes_y_procedimientos.py`
        -   `capitan_politica_y_organizacion.py`
        -   `capitan_preparacion_para_emergencias.py`
        -   `capitan_salud_ocupacional.py`

... (El resto del archivo permanece sin cambios) ...
