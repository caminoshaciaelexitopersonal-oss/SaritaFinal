import * as os from 'os';
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

/**
 * HARDWARE INTELLIGENCE - DESKTOP (HALLAZGO IA LOCAL)
 * Determina la capacidad del equipo para seleccionar el modelo de IA (Ollama) adecuado.
 */

export interface HardwareSpecs {
  os: string;
  ramGB: number;
  cpuCores: number;
  hasOllama: boolean;
  recommendedModel: string;
}

export const getHardwareSpecs = async (): Promise<HardwareSpecs> => {
  const totalMemory = os.totalmem() / (1024 ** 3); // RAM en GB
  const cpuCores = os.cpus().length;
  let hasOllama = false;

  try {
    const { stdout } = await execAsync('ollama --version');
    hasOllama = stdout.includes('ollama');
  } catch (e) {
    hasOllama = false;
  }

  // Lógica de selección de modelo (LM) basada en capacidad
  let recommendedModel = 'phi3'; // Ligero por defecto

  if (totalMemory >= 16 && cpuCores >= 8) {
    recommendedModel = 'llama3:8b'; // Gama Alta
  } else if (totalMemory >= 8) {
    recommendedModel = 'mistral'; // Gama Media
  } else {
    recommendedModel = 'tinyllama'; // Gama Baja
  }

  return {
    os: os.platform(),
    ramGB: Math.round(totalMemory),
    cpuCores,
    hasOllama,
    recommendedModel
  };
};
