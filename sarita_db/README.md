# SARITA ERP - Gestión Financiera Real (Fase 10.9)

## Cerebro Financiero y Control de Liquidez

Este módulo implementa la capa de planeación, control y proyección financiera de SARITA, separada de la contabilidad para permitir una gestión ágil de tesorería e inversiones.

### Estructura de Submódulos

- `01_tesoreria/`: Control real de dinero en cajas, bancos y billeteras digitales.
- `02_presupuestos/`: Planificación con control de versiones y seguimiento de ejecución vs planeado.
- `03_flujo_caja/`: Proyecciones determinísticas y análisis de brechas de liquidez (gaps).
- `04_financiamiento/`: Gestión de deuda, préstamos y líneas de crédito.
- `05_inversiones/`: Seguimiento de rendimientos y movimientos en activos financieros.
- `06_gastos/`: Control administrativo de gastos con soporte para validación de comprobantes (OCR).
- `07_indicadores/`: KPIs financieros y snapshots históricos de salud económica.
- `08_consolidacion/`: Soporte para holdings y reportes consolidados multi-empresa.

## Reglas de Oro Financieras

1. **Separación Contable**: Los movimientos financieros reflejan el flujo real de dinero, mientras que la contabilidad (35) registra la realidad legal/tributaria.
2. **Respaldo de Egreso**: Todo egreso de caja debe disparar una alerta si no existe un asiento contable que lo respalde (validación de integridad).
3. **Inmutabilidad de Presupuestos**: Los presupuestos aprobados no se sobrescriben; se generan nuevas versiones con registro de cambios.
4. **Alimentación IA**: El flujo de caja y los KPIs alimentan constantemente a los agentes de IA para predicción de riesgo y optimización de capital.
