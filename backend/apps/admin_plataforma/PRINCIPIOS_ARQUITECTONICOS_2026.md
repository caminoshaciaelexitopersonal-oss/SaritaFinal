# PRINCIPIOS ARQUITECTÓNICOS NO NEGOCIABLES — 2026

Estos principios rigen la consolidación estructural del sistema y deben ser respetados en cada refactorización.

---

## 🏛️ PRINCIPIO 1: NÚCLEO ÚNICO DE VERDAD
`core_erp` es el único lugar donde reside el conocimiento del dominio financiero, contable y operativo compartido.
*   Cualquier lógica que se repita en dos o más dominios (Holding/Tenants) **debe** ser extraída a `core_erp`.

## 🏛️ PRINCIPIO 2: AISLAMIENTO DE IMPLEMENTACIÓN (INTERFACES)
Ningún módulo puede importar una implementación concreta de otro módulo externo.
*   La comunicación entre dominios se realiza exclusivamente a través de **Interfaces de Servicio** formalizadas o mediante el **EventBus**.

## 🏛️ PRINCIPIO 3: PROHIBICIÓN DE CLONACIÓN FUNCIONAL
No se permiten "mirrors" o clones de lógica de negocio.
*   Si una funcionalidad de `mi_negocio` se requiere en `admin_plataforma`, no se copia; se abstrae y se consume como un servicio compartido.

## 🏛️ PRINCIPIO 4: DESACOPLAMIENTO DE LA INTELIGENCIA (IA)
Los Agentes de IA (`sarita_agents`) no conocen el ORM ni las tablas de base de datos.
*   La IA consume servicios y emite intenciones; nunca realiza queries directas a los modelos de negocio.

## 🏛️ PRINCIPIO 5: ENTIDADES SOBERANAS
La Holding (Admin) y los Tenants son entidades lógica y físicamente separadas.
*   Comparten motores (`core_erp`), pero sus datos y reglas específicas de negocio están aislados.

## 🏛️ PRINCIPIO 6: ESTANDARIZACIÓN TÉCNICA (RCS)
Todo nuevo desarrollo o refactorización debe cumplir con:
*   Naming: **Technical English**.
*   Primary Keys: **UUID v4**.
*   Auditoría: Herencia obligatoria de `BaseErpModel`.

---
**Aprobado por la Dirección Técnica**
*Fase de Consolidación Estructural 2026*
