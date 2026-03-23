import * as LocalAuthentication from 'expo-local-authentication';

/**
 * Hallazgo 12 & Fase 03: Firma y Validación Biométrica
 */

export const securityService = {
  async authenticate() {
    const hasHardware = await LocalAuthentication.hasHardwareAsync();
    const isEnrolled = await LocalAuthentication.isEnrolledAsync();

    if (!hasHardware || !isEnrolled) return true; // Fallback a pass si no hay biometría

    const result = await LocalAuthentication.authenticateAsync({
      promptMessage: 'Confirma tu identidad para continuar',
      fallbackLabel: 'Usar contraseña'
    });

    return result.success;
  }
};
