import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptores para manejar tokens si es necesario
api.interceptors.request.use((config) => {
  if (typeof window !== 'undefined') {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
  }
  return config;
});

export default api;

// --- Tipos y Funciones Placeholder para permitir compilación ---

export interface Categoria {
    id: number;
    nombre: string;
    slug: string;
}

export interface PrestadorPublico {
    id: number;
    nombre_negocio: string;
    categoria_nombre: string;
    foto_principal: string | null;
    municipio_nombre: string;
}

export interface PrestadorPublicoDetalle extends PrestadorPublico {
    descripcion: string;
    telefono_contacto: string;
    email_contacto: string;
    direccion: string;
    latitud: number | null;
    longitud: number | null;
}

export interface Location {
    id: number;
    latitud: number;
    longitud: number;
    nombre: string;
}

export interface FacturaVenta {
    id: string;
    numero_factura: string;
    cliente_nombre: string;
    fecha_emision: string;
    total: string;
    estado_display: string;
}

export interface PaginatedResponse<T> {
    count: number;
    next: string | null;
    previous: string | null;
    results: T[];
}

export const getCategorias = async (): Promise<Categoria[]> => {
    const response = await api.get('/categorias/');
    return response.data;
};

export const getPrestadores = async (categoria?: string, search?: string): Promise<PrestadorPublico[]> => {
    const response = await api.get('/prestadores/', { params: { categoria, search } });
    return response.data;
};

export const getPrestadorById = async (id: number): Promise<PrestadorPublicoDetalle> => {
    const response = await api.get(`/prestadores/${id}/`);
    return response.data;
};

export const getLocations = async (): Promise<Location[]> => {
    const response = await api.get('/locations/');
    return response.data;
};
