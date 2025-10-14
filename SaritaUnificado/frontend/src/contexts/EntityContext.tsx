'use client';

import React, { createContext, useState, useContext, ReactNode, useCallback } from 'react';
import api from '@/lib/api';

interface Entity {
  id: string;
  name: string;
  logo: string | null;
  primary_color: string;
  settings: Record<string, any>;
}

interface EntityContextType {
  entity: Entity | null;
  loadEntity: () => Promise<void>;
  clearEntity: () => void;
}

const EntityContext = createContext<EntityContextType | undefined>(undefined);

export const EntityProvider = ({ children }: { children: ReactNode }) => {
  const [entity, setEntity] = useState<Entity | null>(null);

  const loadEntity = useCallback(async () => {
    try {
      const response = await api.get<Entity>('/admin/my-entity/');
      setEntity(response.data);
    } catch (error) {
      console.error("No se pudo cargar la entidad o el usuario no es admin de una.", error);
      setEntity(null);
    }
  }, []);

  const clearEntity = () => {
    setEntity(null);
  };

  const value = {
    entity,
    loadEntity,
    clearEntity,
  };

  return (
    <EntityContext.Provider value={value}>
      {children}
    </EntityContext.Provider>
  );
};

export const useEntity = () => {
  const context = useContext(EntityContext);
  if (context === undefined) {
    throw new Error('useEntity must be used within an EntityProvider');
  }
  return context;
};