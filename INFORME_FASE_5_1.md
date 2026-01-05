# INFORME DE AUDITORÍA Y DECLARACIÓN ARQUITECTÓNICA – FASE 5.1: MÓDULO DE NÓMINA

## 1. Introducción

Este informe presenta los resultados de la auditoría de verificación realizada sobre el módulo de Nómina, ubicado en `backend/apps/prestadores/mi_negocio/gestion_contable/nomina/`, como parte de la **Fase 5.1** de la Directriz Maestra.

El objetivo de esta auditoría fue analizar el estado y la funcionalidad actual del módulo **sin realizar ninguna modificación en el código**, para establecer su rol arquitectónico y definir un contrato de uso claro para las fases subsecuentes del proyecto.

## 2. Análisis Funcional y Arquitectónico

Se ha realizado una revisión exhaustiva de los componentes del módulo, incluyendo `models.py`, `views.py` y `serializers.py`. A continuación se detallan los hallazgos en respuesta a las preguntas clave de la directiva.

### 2.1. ¿Qué cálculos realiza el módulo?

El módulo **no realiza cálculos automáticos de nómina**. Su única capacidad de cálculo se encuentra en el `PlanillaSerializer`, que determina los totales de una planilla (`total_devengado`, `total_deduccion`, `total_neto`) a partir de la suma de los registros de `NovedadNomina` que son introducidos manualmente por el usuario. Es, en esencia, una calculadora que suma valores pre-calculados externamente.

### 2.2. ¿Qué NO calcula el módulo?

El sistema es un registro pasivo de datos y **no calcula ninguno de los siguientes conceptos críticos de nómina**:
- Salario base según el contrato.
- Pagos por horas extras, recargos nocturnos, festivos, etc.
- Aportes a seguridad social (salud, pensión).
- Aportes parafiscales (SENA, ICBF, Caja de Compensación).
- Provisiones de prestaciones sociales (cesantías, intereses sobre cesantías, prima, vacaciones).
- Retención en la fuente.
- Ingreso Base de Cotización (IBC).

### 2.3. ¿Cómo se registra contablemente la nómina?

El módulo **no tiene ninguna integración con el sistema contable**. No genera `AsientosContables` ni interactúa de ninguna forma con el módulo `gestion_contable/contabilidad`. El registro contable de la nómina debería realizarse de forma manual.

### 2.4. ¿De qué otros módulos depende?

El módulo tiene una dependencia directa y crucial con `gestion_operativa` a través del modelo `ProviderProfile` (`apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models`). Esta dependencia es fundamental para garantizar el correcto funcionamiento de la arquitectura multi-tenancy.

### 2.5. Cumplimiento de Principios Arquitectónicos

- **Multi-tenancy:** **CUMPLE**. El módulo está correctamente diseñado para aislar los datos por prestador de servicios. Los modelos principales (`Empleado`, `Planilla`) están vinculados al `ProviderProfile` del usuario autenticado.
- **Partida Doble:** **NO CUMPLE**. Al no tener integración contable, este principio no se aplica ni se respeta.
- **Periodicidad:** **CUMPLE PARCIALMENTE**. El modelo `Planilla` incluye campos de `periodo_inicio` y `periodo_fin`, lo que permite registrar la periodicidad de la liquidación. Sin embargo, no existe lógica de negocio que automatice, valide o gestione estos periodos.

## 3. Declaración Arquitectónica: Rol Transitorio

Se declara formalmente que el módulo de Nómina, en su estado actual, es un **esqueleto funcional y un módulo de registro pasivo**.

- **Rol Arquitectónico:** Su rol es **TRANSITORIO**. Sirve como un contenedor de datos básico para que los prestadores puedan registrar los totales de sus liquidaciones de nómina, manteniendo la integridad referencial y la separación por tenant.
- **Deuda Técnica:** Se reconoce la existencia de una deuda técnica significativa. El módulo carece de la lógica de negocio indispensable para ser considerado un sistema de liquidación de nómina funcional.
- **Propósito Actual:** Su único propósito en el estado actual del proyecto es habilitar la construcción de la interfaz de usuario (Fase 5.2) y almacenar datos pre-calculados, evitando que el desarrollo del frontend se bloquee.

## 4. Contrato de Uso para la Fase 5.2 (Integración UI)

Para la siguiente fase de desarrollo, el módulo de nómina deberá ser utilizado bajo las siguientes condiciones:

1.  **Entrada de Datos Manual:** El frontend debe ser diseñado asumiendo que el usuario realizará todos los cálculos de devengados y deducciones por fuera del sistema "Sarita".
2.  **Endpoints CRUD:** La integración se limitará a consumir los `ViewSet` existentes para crear, leer, actualizar y eliminar (`CRUD`) empleados, contratos y planillas.
3.  **Lógica de Negocio Cero:** No se debe intentar implementar ninguna lógica de cálculo en el frontend. El frontend actuará como un simple formulario para capturar los resultados de los cálculos externos.
4.  **Enfoque en UI/UX:** El objetivo de la Fase 5.2 será exclusivamente proporcionar una interfaz para que el usuario pueda interactuar con los modelos existentes.

## 5. Recomendación Post-Fase 6

Se recomienda de manera explícita que, una vez finalizada la Fase 6 de estabilización e integración, se planifique una **refactorización completa** del módulo de nómina. Este nuevo módulo deberá incluir:

- Un motor de cálculo robusto que cumpla con la normativa laboral colombiana.
- Integración total y automática con el módulo de contabilidad para la generación de asientos contables.
- Conexión con el módulo financiero para registrar los pagos de nómina.

## 6. Conclusión

La auditoría de la Fase 5.1 ha concluido con éxito. Se ha analizado el módulo de nómina en su totalidad y se ha documentado su estado actual sin realizar modificaciones. Este informe establece las bases, limitaciones y el camino a seguir para su integración y futura evolución dentro del ecosistema "Sarita". Se confirma que no se ha modificado ningún archivo de código de la aplicación durante esta fase.
