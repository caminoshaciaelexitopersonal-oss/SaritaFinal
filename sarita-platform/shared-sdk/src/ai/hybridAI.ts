import axios from 'axios';
import { httpClient } from '../api/httpClient';

/**
 * HYBRID AI ENGINE (EDGE AI) - SHARED SDK
 * Gestiona el flujo entre IA remota (Backend) e IA local (Ollama).
 */

export interface AIResponse {
  answer: string;
  source: 'REMOTE' | 'LOCAL';
  model: string;
}

class HybridAIEngine {
  private localOllamaURL: string = 'http://localhost:11434/api/generate';
  private currentModel: string = 'phi3';

  public setLocalConfig(model: string, url?: string) {
    this.currentModel = model;
    if (url) this.localOllamaURL = url;
  }

  /**
   * Procesa una orden o consulta intentando primero el backend,
   * y cayendo a Ollama local si no hay conexión.
   */
  async ask(query: string): Promise<AIResponse> {
    try {
      // 1. Intento Remoto (Backend)
      const response = await httpClient.post('/ai/assistant/', { query });
      return {
        answer: response.data.answer,
        source: 'REMOTE',
        model: response.data.model
      };
    } catch (error) {
      console.warn('AI SDK: Backend inalcanzable. Cayendo a IA Local (Ollama)...');

      // 2. Intento Local (Edge AI)
      try {
        const localResponse = await axios.post(this.localOllamaURL, {
          model: this.currentModel,
          prompt: query,
          stream: false
        }, { timeout: 30000 });

        return {
          answer: localResponse.data.response,
          source: 'LOCAL',
          model: this.currentModel
        };
      } catch (localError) {
        throw new Error('AI SDK: Fallo total. Ni el backend ni Ollama local están disponibles.');
      }
    }
  }
}

export const hybridAI = new HybridAIEngine();
