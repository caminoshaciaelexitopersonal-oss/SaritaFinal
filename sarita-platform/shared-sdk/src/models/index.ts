/**
 * Definiciones de Modelos de Datos Unificados para SARITA
 * (Principio: Un solo cerebro, muchos cuerpos)
 */

export interface User {
  id: string;
  email: string;
  first_name: string;
  last_name: string;
  role: 'admin' | 'operator' | 'provider' | 'tourist';
}

export interface Tour {
  id: string;
  name: string;
  description: string;
  price: number;
  location: {
    latitude: number;
    longitude: number;
    address: string;
  };
  rating: number;
  provider_id: string;
}

export interface Reservation {
  id: string;
  tour_id: string;
  user_id: string;
  status: 'pending' | 'confirmed' | 'cancelled' | 'completed';
  date: string;
  total_price: number;
}
