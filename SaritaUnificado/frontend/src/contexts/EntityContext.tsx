'use client';

import React, { createContext, useState, useContext, ReactNode, useCallback, useEffect } from 'react';
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
  isLoading: boolean;
}

const EntityContext = createContext<EntityContextType | undefined>(undefined);

export const EntityProvider = ({ children }: { children: ReactNode }) => {
  const [entity, setEntity] = useState<Entity | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchEntity = async () => {
      setIsLoading(true);
      try {
        const response = await api.get<Entity>('/entities/current/');
        if (response.data) {
          setEntity(response.data);
        } else {
          setEntity(null);
        }
      } catch (error) {
        console.error("No se pudo determinar la entidad actual desde el subdominio.", error);
        setEntity(null);
      } finally {
        setIsLoading(false);
      }
    };

    fetchEntity();
  }, []);

  const value = {
    entity,
    isLoading,
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