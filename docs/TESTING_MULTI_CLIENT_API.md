# GUÍA DE PRUEBAS DE INTEGRACIÓN MULTI-CLIENTE (API SARITA)

**Fase:** Validación Multi-Client del Ecosistema
**Objetivo:** Garantizar que el backend Django responda correctamente a clientes Web, Mobile y Desktop bajo el estándar RS256.

---

## 1. PRUEBAS DE AUTENTICACIÓN (JWT RS256)

El backend requiere el encabezado `Authorization: Bearer <token>` para clientes no-web.

### Prueba con cURL
```bash
curl -X POST http://localhost:8000/api/v1/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{"email": "admin@example.com", "password": "admin"}'
```

### Validación del Token
Utilice [jwt.io](https://jwt.io) para verificar que el token recibido contiene los claims correctos:
- `user_id`
- `role`
- `exp` (Tiempo de expiración)

---

## 2. PRUEBAS DE CONEXIÓN MOBILE (React Native)

Para simular la conexión desde la app móvil, verifique los siguientes escenarios:

### Escenario: Conexión Inicial (Auth)
1.  **Entorno:** Configurar `EXPO_PUBLIC_API_URL` en el archivo `.env`.
2.  **Acción:** Intentar login desde el simulador/dispositivo físico.
3.  **Validación:** El backend debe registrar la conexión y emitir un evento `USER_LOGGED_IN` en el `EventAuditLog`.

### Escenario: Sincronización Offline
1.  **Acción:** Desactivar Wi-Fi/Datos en el dispositivo.
2.  **Acción:** Realizar una "Venta Rápida".
3.  **Validación:** La transacción debe guardarse en la tabla `sync_queue` de SQLite localmente.
4.  **Acción:** Reactivar conexión.
5.  **Validación:** El servicio de sincronización debe disparar el POST al backend.

---

## 3. PRUEBAS DE CONEXIÓN DESKTOP (Electron)

### Escenario: IPC Bridge
1.  **Acción:** Desde el proceso renderer, llamar a `window.electronAPI.sendMessage('auth', credentials)`.
2.  **Validación:** El proceso main debe recibir los datos y usar el `Shared SDK` para comunicarse con la API.

---

## 4. CONSIDERACIONES DE SEGURIDAD (CORS)

Asegúrese de que el backend permita los orígenes de las nuevas capas.

**Archivo:** `backend/puerto_gaitan_turismo/settings.py`

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",      # Web
    "http://localhost:19006",     # Expo Web
    "ms-appx://",                 # Windows Desktop
    "capacitor://",               # Mobile WebView
]
```

---

## 5. REPORTE DE RESULTADOS ESPERADOS

| Caso de Prueba | Resultado Web | Resultado Mobile | Resultado Desktop |
| :--- | :---: | :---: | :---: |
| Login con JWT | Exitoso | Exitoso | Exitoso |
| Consulta Atractivos | Exitoso | Exitoso | Exitoso |
| Notificación Push | No Aplica | Exitoso | Pendiente |
| Registro Venta | Exitoso | Exitoso (Sync) | Exitoso |

---
**Elaborado por:** Jules (AI Senior Engineer)
