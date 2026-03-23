'use client';

import React, { createContext, useState, useContext, ReactNode, useCallback, useEffect } from 'react';
import api from '@/services/api';

export interface Entity {
  id: string;
  name: string;
  logo: string | null;
  primary_color: string;
  settings: Record<string, unknown>;
}

interface EntityContextType {
  entity: Entity | null;
  isLoading: boolean;
  loadEntity: (entityId?: string) => Promise<void>;
  switchEntity: (entityId: string) => Promise<void>;
  clearEntity: () => void;
}

const EntityContext = createContext<EntityContextType | undefined>(undefined);

export const EntityProvider = ({ children }: { children: ReactNode }) => {
  const [entity, setEntity] = useState<Entity | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // 🔹 Cargar entidad automáticamente desde el subdominio o localStorage
  useEffect(() => {
    const fetchInitialEntity = async () => {
      if (typeof window === 'undefined') return;

      const storedEntityId = localStorage.getItem('activeCompanyId');

      if (storedEntityId) {
        await loadEntity(storedEntityId);
        return;
      }

      // Fallback: subdominio (solo si no es localhost)
      if (window.location.hostname !== 'localhost') {
        setIsLoading(true);
        try {
          const response = await api.get<Entity>('/entities/current/');
          if (response.data) {
            setEntity(response.data);
            localStorage.setItem('activeCompanyId', response.data.id);
          }
        } catch (error) {
          console.error('S-UCE: Fallo en resolución de entidad por subdominio.', error);
        } finally {
          setIsLoading(false);
        }
      } else {
        setIsLoading(false);
      }
    };

    fetchInitialEntity();
  }, []);

  // 🔹 Función para cargar una entidad específica o la asignada al usuario
  const loadEntity = useCallback(async (entityId?: string) => {
    setIsLoading(true);
    try {
      const url = entityId ? `/entities/${entityId}/` : '/admin/my-entity/';
      const response = await api.get<Entity>(url);
      setEntity(response.data);
      if (typeof window !== 'undefined') {
        localStorage.setItem('activeCompanyId', response.data.id);
      }
    } catch (error) {
      console.error('S-UCE: No se pudo cargar la entidad operativa.', error);
      setEntity(null);
    } finally {
      setIsLoading(false);
    }
  }, []);

  // 🔹 Función para cambiar de entidad (Multi-tenant switch)
  const switchEntity = useCallback(async (entityId: string) => {
    await loadEntity(entityId);
    if (typeof window !== 'undefined') {
      window.location.reload(); // Sincronización pesada para asegurar hidratación de todos los motores
    }
  }, [loadEntity]);

  // 🔹 Función para limpiar la entidad actual
  const clearEntity = useCallback(() => {
    setEntity(null);
    if (typeof window !== 'undefined') {
      localStorage.removeItem('activeCompanyId');
    }
  }, []);

  const value = {
    entity,
    isLoading,
    loadEntity,
    switchEntity,
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