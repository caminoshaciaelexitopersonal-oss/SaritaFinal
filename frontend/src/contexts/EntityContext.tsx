'use client';

import React, { createContext, useState, useContext, ReactNode, useCallback, useEffect } from 'react';
import api from '@/services/api';

interface Entity {
  id: string;
  name: string;
  logo: string | null;
  primary_color: string;
  settings: Record<string, unknown>;
}

interface EntityContextType {
  entity: Entity | null;
  isLoading: boolean;
  loadEntity: () => Promise<void>;
  clearEntity: () => void;
}

const EntityContext = createContext<EntityContextType | undefined>(undefined);

export const EntityProvider = ({ children }: { children: ReactNode }) => {
  const [entity, setEntity] = useState<Entity | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // 🔹 Cargar entidad automáticamente desde el subdominio
  useEffect(() => {
    const fetchEntity = async () => {
      // FIX: En desarrollo (localhost), no hay subdominio, por lo que esta llamada siempre falla.
      // Omitimos la llamada para permitir que la aplicación se renderice correctamente.
      if (typeof window !== 'undefined' && window.location.hostname === 'localhost') {
        setIsLoading(false);
        return;
      }

      setIsLoading(true);
      try {
        const response = await api.get<Entity>('/entities/current/');
        if (response.data) {
          setEntity(response.data);
        } else {
          setEntity(null);
        }
      } catch (error) {
        console.error('No se pudo determinar la entidad actual desde el subdominio.', error);
        setEntity(null);
      } finally {
        setIsLoading(false);
      }
    };

    fetchEntity();
  }, []);

  // 🔹 Función para que el administrador cargue su entidad manualmente
  const loadEntity = useCallback(async () => {
    try {
      const response = await api.get<Entity>('/admin/my-entity/');
      setEntity(response.data);
    } catch (error) {
      console.error('No se pudo cargar la entidad o el usuario no es admin de una.', error);
      setEntity(null);
    }
  }, []);

  // 🔹 Función para limpiar la entidad actual
  const clearEntity = () => {
    setEntity(null);
  };

  const value = {
    entity,
    isLoading,
    loadEntity,
    clearEntity,
  };

  return <EntityContext.Provider value={value}>{children}</EntityContext.Provider>;
};

export const useEntity = (): EntityContextType => {
  const context = useContext(EntityContext);
  if (!context) {
    throw new Error('useEntity debe usarse dentro de un EntityProvider');
  }
  return context;
};