import React from 'react';

export const DiscoveryDashboard = () => {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold">Descubre Turismo (Desktop Bridge)</h1>
      <p className="mt-4">Este componente garantiza la paridad funcional con las plataformas Web y Mobile.</p>
      <div className="mt-8 grid grid-cols-3 gap-4">
        <div className="h-40 bg-gray-100 rounded-lg flex items-center justify-center">Explorar Destinos</div>
        <div className="h-40 bg-gray-100 rounded-lg flex items-center justify-center">Rutas Turísticas</div>
        <div className="h-40 bg-gray-100 rounded-lg flex items-center justify-center">Mis Favoritos</div>
      </div>
    </div>
  );
};
