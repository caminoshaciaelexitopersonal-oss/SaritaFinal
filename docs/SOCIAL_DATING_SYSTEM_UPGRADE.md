# ACTUALIZACIÓN DEL SISTEMA SOCIAL Y DE CITAS (VÍA 3)

**Fecha:** Marzo 2026
**Responsable:** Jules (AI Engineer)
**Estado:** CERTIFICADO - PRODUCCIÓN REAL

## 1. VISION GENERAL
El sistema de chat de la Vía 3 (Ciudadanos/Turistas) ha sido transformado en una **Super App Social y de Citas** completamente funcional. Aparte de la comunicación institucional, ahora permite interacciones sociales avanzadas, video citas y monetización mediante regalos.

---

## 2. COMPONENTES DEL MOTOR SOCIAL

### A. Salas de Video Citas
- **Públicas:** Disponibles para descubrimiento general.
- **Privadas:** Requieren el pago de una tarifa de entrada (`entry_fee`) definida por el creador. El acceso se procesa mediante el `WalletService` en tiempo real.
- **Restricción de Edad:** Validación automática basada en la fecha de nacimiento del usuario. Solo mayores de 18 años pueden crear o unirse a salas marcadas como `is_adult_only`.

### B. Perfiles Multimedia Avanzados
- **Presentación:** Los turistas cuentan con fotos y videos de presentación en su perfil.
- **Galería:** Soporte para múltiples archivos de imagen y video (`SocialProfileMedia`).
- **Dating Activo:** Switch para habilitar/deshabilitar la visibilidad en el módulo de citas.

### C. Motor de Regalos Económicos (Monetización)
- **Catálogo:** 20 niveles de regalos desde $5.000 hasta $100.000 COP.
- **Lógica de Comisión:**
  - El sistema cobra un **2% de comisión** sobre el valor del regalo.
  - La comisión **aumenta el valor** que paga el emisor (Ej: Regalo de $5.000 -> Emisor paga $5.100).
  - Distribución: El receptor obtiene el valor base ($5.000) y el Super Admin obtiene la comisión ($100).
  - Integración: Procesado mediante transacciones complejas en `wallet_db`.

---

## 3. PARIDAD MULTIPLATAFORMA

### Web (Next.js 15)
- Nueva interfaz de Super App Social en `/dashboard/social`.
- Flujos integrados para creación de salas y envío de regalos.

### Mobile (Expo 52)
- Pantalla `ChatScreen.tsx` actualizada con insignias de video y tienda de regalos modal.
- Nueva pantalla `SocialProfileScreen.tsx` para visualizar perfiles multimedia.
- `socialService.ts` implementado para comunicación con el backend real.

### Desktop (Electron 33)
- Módulo `SocialModule.tsx` dedicado en el renderer.
- Soporte para video rooms y store de regalos lateral.

---

## 4. SEGURIDAD Y CUMPLIMIENTO
- **Integridad Financiera:** Uso de `select_for_update` y transacciones atómicas para garantizar que los regalos y tarifas de entrada no dupliquen o pierdan fondos.
- **Control de Acceso:** Decorador `adult_only_required` aplicado a nivel de API para proteger funciones sensibles.

---

## 5. CONCLUSIÓN
La Vía 3 cuenta ahora con un ecosistema social soberano, seguro y monetizable, eliminando cualquier dependencia de simulaciones y garantizando una experiencia de usuario de nivel producción en todas las plataformas.
