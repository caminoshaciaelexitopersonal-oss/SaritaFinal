'use client';

import React from 'react';
import { FiDollarSign } from 'react-icons/fi';

const GestionContablePlaceholder = () => {
  return (
    <div className="flex flex-col items-center justify-center h-full p-8 text-center bg-white rounded-lg shadow-md">
      <FiDollarSign className="w-16 h-16 mb-4 text-gray-300" />
      <h2 className="text-2xl font-bold text-gray-800">Módulo de Gestión Contable</h2>
      <p className="mt-2 text-gray-500">
        Esta sección se encuentra en desarrollo y estará disponible en futuras versiones.
      </p>
      <p className="mt-1 text-sm text-gray-400">
        Aquí podrás gestionar facturación, informes financieros y más.
      </p>
    </div>
  );
};

export default GestionContablePlaceholder;