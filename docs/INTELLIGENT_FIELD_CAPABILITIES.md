# CAPACIDADES INTELIGENTES DE CAMPO (FASE DE ACTIVACIÓN)

**Estado:** Activado (Estructura y Servicios Base)
**Hallazgos Cubiertos:** 10 (Push Notifications), 11 (Geofencing), 12 (Digital Signature)

---

## 1. SISTEMA DE NOTIFICACIONES PUSH (HALLAZGO 10)

El sistema utiliza **Firebase Cloud Messaging (FCM)** para la entrega de alertas en tiempo real hacia los dispositivos móviles de prestadores y turistas.

### Componentes Implementados:
- **Modelo Backend:** `DeviceToken` en `backend/api/models.py` para registro de tokens.
- **Servicio Backend:** `notification_service.py` para despacho de mensajes desde el servidor Django.
- **Servicio Mobile:** `pushNotificationService.ts` utilizando `expo-notifications` para solicitar permisos y obtener el token de dispositivo.

### Casos de Uso:
1.  **Nueva Reserva:** Alerta inmediata al prestador cuando entra una compra.
2.  **Confirmación de Pago:** Notificación al turista de que su pago ha sido procesado.

---

## 2. SISTEMA DE GEOFENCING TURÍSTICO (HALLAZGO 11)

Permite la detección proactiva de turistas cerca de los puntos de interés o servicios de los prestadores para disparar ofertas y alertas de seguridad.

### Componentes Implementados:
- **Modelo Backend:** `ServiceLocation` para definir el radio de la geocerca.
- **Motor de Geocercas:** `geofence_engine.py` utiliza la fórmula de **Haversine** para calcular distancias en tiempo real entre coordenadas GPS.
- **Servicio Mobile:** `geofenceService.ts` utilizando `expo-location` para el rastreo de coordenadas.

---

## 3. SISTEMA DE FIRMA DIGITAL MÓVIL (HALLAZGO 12)

Habilita la captura de firmas legales con validación biométrica directamente desde el dispositivo móvil, garantizando la integridad documental.

### Componentes Implementados:
- **Biometría:** `signatureService.ts` utilizando `expo-local-authentication` para Face ID y Huella Dactilar.
- **Captura de Firma:** Integración de `react-native-signature-canvas`.
- **Integridad:** Las firmas se registran con el hash del documento y un timestamp en el sistema archivístico SARITA.

### Proceso de Firma:
1.  El usuario previsualiza el contrato.
2.  El sistema solicita **autenticación biométrica**.
3.  El usuario firma en el canvas digital.
4.  La firma se transmite al backend para su almacenamiento archivístico legal.

---
**Elaborado por:** Jules (AI Senior Engineer)
