import * as LocalAuthentication from 'expo-local-authentication';

/**
 * Hallazgo 12: Firma Digital Móvil.
 * Valida la identidad del usuario mediante biometría antes de autorizar firmas digitales.
 */

export async function checkBiometryAvailability() {
  const compatible = await LocalAuthentication.hasHardwareAsync();
  const enrolled = await LocalAuthentication.isEnrolledAsync();
  const types = await LocalAuthentication.supportedAuthenticationTypesAsync();

  return { compatible, enrolled, types };
}

export async function authenticateWithBiometrics(promptMessage: string = 'Confirma tu identidad para firmar el documento') {
  const result = await LocalAuthentication.authenticateAsync({
    promptMessage,
    fallbackLabel: 'Usar contraseña',
    cancelLabel: 'Cancelar',
    disableDeviceFallback: false,
  });

  if (result.success) {
    console.log('SARITA Biometry: Identidad verificada con éxito.');
    return true;
  } else {
    console.warn('SARITA Biometry: Error en la autenticación biométrica:', result.error);
    return false;
  }
}

export async function processDigitalSignature(signatureBase64: string, documentId: string, api: any) {
  try {
    // Registra la firma digital con hash SHA-256 en el sistema archivístico SARITA
    const response = await api.post('/v1/archivos/firma-digital/', {
      document_id: documentId,
      signature: signatureBase64,
      verification_type: 'biometric',
      timestamp: new Date().toISOString()
    });
    return response.data;
  } catch (error) {
    console.error('SARITA Archivos: Error registrando firma digital:', error);
    return null;
  }
}
