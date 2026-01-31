'use client';

import { useState, useCallback } from 'react';
import { SADIState } from '../ui/components/feedback/SADIVoiceLayer';
import { voiceEndpoints } from '@/services/endpoints/voice';

export function useSADI() {
  const [state, setState] = useState<SADIState>('idle');
  const [responseMessage, setResponseMessage] = useState<string>('');
  const [lastIntent, setLastIntent] = useState<any>(null);
  const [confirmationData, setConfirmationData] = useState<{ message: string, actionId: string } | null>(null);
  const pollingRef = useRef<NodeJS.Timeout | null>(null);

  const pollMission = useCallback(async (missionId: string) => {
    if (pollingRef.current) clearInterval(pollingRef.current);

    pollingRef.current = setInterval(async () => {
      try {
        const res = await voiceEndpoints.getMissionStatus(missionId);
        const { estado, reporte_final } = res.data;

        if (estado === 'COMPLETADA' || estado === 'FALLIDA') {
          if (pollingRef.current) clearInterval(pollingRef.current);
          setResponseMessage(reporte_final || `Misión terminada con estado: ${estado}`);
          setState(estado === 'COMPLETADA' ? 'success' : 'error');
          setTimeout(() => setState('idle'), 5000);
        }
      } catch (err) {
        if (pollingRef.current) clearInterval(pollingRef.current);
        setState('error');
      }
    }, 2000);
  }, []);

  const processAudio = useCallback(async (audioBlob: Blob) => {
    setState('processing');
    setResponseMessage('');

    try {
      const response = await voiceEndpoints.sendAudio(audioBlob);

      const { text, audio_url, intent, requires_confirmation, confirmation_message, action_id, mission_id } = response.data;
      setResponseMessage(text);
      setLastIntent(intent);

      if (requires_confirmation) {
          setConfirmationData({ message: confirmation_message || text, actionId: action_id });
          setState('confirming');
      } else if (mission_id) {
          setState('processing');
          pollMission(mission_id);
      } else {
          setState('success');
          setTimeout(() => setState('idle'), 5000);
      }

      // TTS Playback
      if (audio_url) {
        const audio = new Audio(audio_url);
        audio.play();
      }

      // Reset to idle after 5 seconds
      setTimeout(() => {
        setState('idle');
      }, 5000);

    } catch (err) {
      console.error("SADI processing error", err);
      setState('error');
      setResponseMessage("No pude comprender la instrucción. Por favor, intenta de nuevo.");

      setTimeout(() => {
        setState('idle');
      }, 5000);
    }
  }, []);

  const sendTextIntent = useCallback(async (text: string) => {
    setState('processing');
    try {
        const response = await voiceEndpoints.sendIntent(text);
        const { text: responseText, intent } = response.data;
        setResponseMessage(responseText);
        setLastIntent(intent);
        setState('success');

        setTimeout(() => setState('idle'), 5000);
    } catch (err) {
        setState('error');
        setResponseMessage("Error de conexión con el motor SADI.");
        setTimeout(() => setState('idle'), 5000);
    }
  }, []);

  const confirmAction = useCallback(async () => {
    if (!confirmationData) return;
    setState('processing');
    try {
        await api.post(`/api/voice/actions/${confirmationData.actionId}/confirm/`);
        setState('success');
        setResponseMessage("Acción confirmada y ejecutada.");
        setConfirmationData(null);
    } catch (err) {
        setState('error');
        setResponseMessage("No se pudo confirmar la acción.");
    }
  }, [confirmationData]);

  const cancelAction = useCallback(() => {
    setConfirmationData(null);
    setState('idle');
  }, []);

  return {
    state,
    responseMessage,
    lastIntent,
    confirmationData,
    processAudio,
    sendTextIntent,
    confirmAction,
    cancelAction,
    setState
  };
}
