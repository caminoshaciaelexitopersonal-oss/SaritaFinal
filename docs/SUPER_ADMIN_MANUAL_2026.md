# MANUAL DE OPERACIÓN: SUPER ADMINISTRADOR SARITA (V1.0)

**Fecha:** Marzo 2026
**Responsable:** Jules (AI Engineer)
**Acceso:** Exclusivo para usuarios con Rol `ADMIN` o `Superuser`.

---

## 1. GOBERNANZA Y CONFIGURACIÓN GLOBAL

El Super Admin tiene el control total sobre los parámetros que rigen el comportamiento económico y operativo de la plataforma.

### A. Gestión de Comisiones
- **Social Dating:** Configuración del porcentaje de recaudo para regalos en Vía 3 (Defecto: 2%).
- **Reservas:** Configuración del porcentaje de plataforma para servicios turísticos (Defecto: 10%).
- **Impacto:** Los cambios en estos porcentajes afectan inmediatamente al cálculo en `SocialGiftService` y `CommissionsEngine`.

### B. Modo Mantenimiento
- Interruptor global para restringir el acceso a usuarios finales en caso de actualizaciones críticas o auditorías forenses.

---

## 2. SUPERVISIÓN DE COMPONENTES TRIPLE VÍA

### Vía 3: Social y Dating
- **Auditoría de Salas:** Monitoreo en tiempo real de todas las salas públicas y privadas. Capacidad para auditar el número de participantes y la transparencia de las tarifas de entrada.
- **Auditoría de Regalos:** Registro completo de transacciones económicas entre usuarios, detallando el emisor, receptor, monto base y la comisión retenida para la administración.

### Vía 1: Territorial (DIVIPOLA)
- Control maestro sobre la estructura geográfica (Departamentos y Municipios). Garantiza que todos los registros de usuarios y servicios estén correctamente georeferenciados.

---

## 3. CONTROL FINANCIERO Y CONTABLE (PUC)

### Maestro Global de Cuentas
- Visibilidad cross-tenant de la estructura contable.
- Auditoría de la distribución de cuentas por clase (Activos, Pasivos, Patrimonio, etc.) en todo el ecosistema.
- Asegura el cumplimiento del Decreto 2650 de 1993 en todas las empresas registradas.

---

## 4. AUDITORÍA FORENSE Y SEGURIDAD

- **Forensic Logs:** Acceso a la cadena de hashes inmutable de eventos críticos.
- **Supervisión DIAN:** Monitoreo del estado de la facturación electrónica de todos los prestadores activos.

---

## 5. CONCLUSIÓN
El rol de Super Admin en SARITA no es solo administrativo, sino que actúa como el **Guardián de la Soberanía de la Plataforma**, con herramientas de visibilidad total y ajuste fino sobre cada motor del sistema.
