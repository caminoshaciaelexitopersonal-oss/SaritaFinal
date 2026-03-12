import * as Device from 'expo-device';

/**
 * DEVICE INTELLIGENCE - MOBILE (HALLAZGO IA LOCAL)
 * Evalúa las capacidades del dispositivo móvil para uso de IA local o remota.
 */

export interface MobileSpecs {
  brand: string;
  modelName: string;
  totalMemory: number;
  osName: string;
  iaCapability: 'LOW' | 'MEDIUM' | 'HIGH';
  recommendedModel: string;
}

export const getMobileIntelligence = async (): Promise<MobileSpecs> => {
  const memory = Device.totalMemory ? Device.totalMemory / (1024 ** 3) : 0;

  let iaCapability: 'LOW' | 'MEDIUM' | 'HIGH' = 'LOW';
  let recommendedModel = 'phi3-mini'; // Por defecto ligero

  if (memory >= 8) {
    iaCapability = 'HIGH';
    recommendedModel = 'llama3-7b-q4';
  } else if (memory >= 4) {
    iaCapability = 'MEDIUM';
    recommendedModel = 'phi3';
  }

  return {
    brand: Device.brand || 'unknown',
    modelName: Device.modelName || 'unknown',
    totalMemory: Math.round(memory),
    osName: Device.osName || 'unknown',
    iaCapability,
    recommendedModel
  };
};
