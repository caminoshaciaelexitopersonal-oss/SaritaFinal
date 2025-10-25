'use client';

import React from 'react';
import { useAuth } from '@/contexts/AuthContext';

const DashboardPage = () => {
  const { user, isLoading } = useAuth();

  if (isLoading) {
    return <div className="flex justify-center items-center h-screen">Cargando...</div>;
  }

  if (!user) {
    return (
        <div className="flex justify-center items-center h-screen">
            <p>No estás autorizado para ver esta página.</p>
        </div>
    );
  }

  return (
    <div>
      <h1 className="text-2xl font-bold">Bienvenido a tu Panel de Control</h1>
      <p className="mt-2">Selecciona un módulo del menú de la izquierda para comenzar a gestionar tu negocio.</p>
    </div>
  );
};

export default DashboardPage;