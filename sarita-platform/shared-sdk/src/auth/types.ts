export interface SavedItem {
  id: number;
  content_type_name: string;
  object_id: number;
}

export interface CategoriaPrestador {
  id: number;
  nombre: string;
  slug: string;
}

export interface PrestadorProfile {
  id: number;
  nombre_negocio: string;
  descripcion: string;
  telefono: string;
  email_contacto: string;
  latitud: number;
  longitud: number;
  categoria: CategoriaPrestador;
}

export interface User {
  pk: number;
  username: string;
  email: string;
  role:
    | 'ADMIN'
    | 'ADMIN_ENTIDAD'
    | 'FUNCIONARIO_DIRECTIVO'
    | 'FUNCIONARIO_PROFESIONAL'
    | 'PRESTADOR'
    | 'ARTESANO'
    | 'TURISTA';
  perfil_prestador?: PrestadorProfile;
}

export interface RegisterData {
  username?: string;
  email: string;
  password1: string;
  password2: string;
  role:
    | 'TURISTA'
    | 'PRESTADOR'
    | 'ARTESANO'
    | 'ADMINISTRADOR'
    | 'FUNCIONARIO_DIRECTIVO'
    | 'FUNCIONARIO_PROFESIONAL';
  department_id?: number;
  municipality_id?: number;
  nombre_negocio?: string;
  categoria_id?: number;
  nombre_taller?: string;
  rubro_id?: number;
  cargo?: string;
  dependencia_asignada?: string;
  nivel_acceso?: string;
  dependencia?: string;
  nivel_direccion?: string;
  area_funcional?: string;
  profesion?: string;
  area_asignada?: string;
}
