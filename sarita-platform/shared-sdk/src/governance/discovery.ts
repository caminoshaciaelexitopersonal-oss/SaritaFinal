import { httpClient } from '../api/httpClient';

export interface AttractionData {
  id: string;
  name: string;
  category: string;
  description: string;
  imageUrl: string;
}

export interface RegionalEvent {
  id: string;
  title: string;
  date: string;
  location: string;
}

export class DiscoveryService {
  /**
   * Obtiene la lista de atractivos turísticos.
   */
  static async getAttractions(): Promise<AttractionData[]> {
    const response = await httpClient.get('/atractivos/');
    return response.data.map((a: any) => ({
      id: a.id.toString(),
      name: a.nombre,
      category: a.categoria_color,
      description: a.descripcion,
      imageUrl: a.imagen_principal_url
    }));
  }

  /**
   * Obtiene la agenda cultural regional.
   */
  static async getRegionalEvents(): Promise<RegionalEvent[]> {
    // Nota: Endpoint simulado o a integrar en backend
    const response = await httpClient.get('/descubre/eventos/');
    return response.data;
  }
}
