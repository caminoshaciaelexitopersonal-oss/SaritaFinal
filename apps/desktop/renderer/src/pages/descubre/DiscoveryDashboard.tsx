import React from 'react';

export const DiscoveryDashboard = () => {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Descubre el Territorio</h1>
      <p className="text-gray-600 mb-8">Explora atractivos, rutas y eventos desde tu aplicación de escritorio.</p>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-4 rounded-lg shadow border border-gray-100">
          <div className="h-32 bg-gray-200 rounded-md mb-4 flex items-center justify-center">Atractivos</div>
          <h2 className="font-semibold">Atractivos Turísticos</h2>
          <p className="text-sm text-gray-500">Conoce los lugares más emblemáticos.</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow border border-gray-100">
          <div className="h-32 bg-gray-200 rounded-md mb-4 flex items-center justify-center">Rutas</div>
          <h2 className="font-semibold">Rutas Estratégicas</h2>
          <p className="text-sm text-gray-500">Recorre el territorio con rutas guiadas.</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow border border-gray-100">
          <div className="h-32 bg-gray-200 rounded-md mb-4 flex items-center justify-center">Reservas</div>
          <h2 className="font-semibold">Mis Reservas</h2>
          <p className="text-sm text-gray-500">Gestiona tus planes de viaje.</p>
        </div>
      </div>
    </div>
  );
};
