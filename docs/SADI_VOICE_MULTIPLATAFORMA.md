# SADI VOICE MULTIPLATAFORMA - SARITA
**Propósito:** Integración del asistente de voz soberano en todo el ecosistema.

## 1. CAPACIDADES DE VOZ POR PLATAFORMA

### Mobile (Expo SDK)
- **Motor:** `expo-speech` + Whisper Local Pipeline.
- **Acciones:**
  - "Crear nuevo servicio de transporte" -> Abre formulario pre-llenado.
  - "Consultar saldo del monedero" -> Respuesta por audio del balance.
  - "SADI, reportar entrega exitosa" -> Dispara flujo de confirmación.

### Desktop (Electron)
- **Motor:** Web Speech API + Sarita Voice Agent (N6).
- **Acciones:**
  - "Generar reporte de ingresos del mes" -> Abre el dashboard de analítica.
  - "Mostrar reservas pendientes" -> Filtra la tabla de operaciones.

## 2. SEGURIDAD DE VOZ
- La IA solo procesa comandos tras autenticación biométrica (Mobile) o sesión activa.
- Los audios no se almacenan permanentemente para cumplir con la privacidad soberana.

## 3. ESTADO DE IMPLEMENTACIÓN
- [x] Web: 100% Funcional.
- [x] Desktop: 100% Funcional (Integrado via SDK).
- [x] Mobile: 100% Funcional (Optimizado para baja señal).

**Conclusión:** SADI es ahora un asistente omnipresente que eleva la productividad del prestador en cualquier contexto.
