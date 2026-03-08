import React from 'react';

export const BusinessManager = () => (
  <div className="space-y-6">
    <div className="bg-white p-8 rounded-lg shadow-sm">
      <h2 className="text-xl font-bold text-primary mb-4">Gestión Mi Negocio (ERP)</h2>
      <p className="text-gray-600 mb-8">Administra tus servicios turísticos, reservas y clientes desde esta central operativa.</p>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="border p-6 rounded-lg hover:border-primary transition cursor-pointer">
          <h3 className="font-bold mb-2">Servicios Activos</h3>
          <p className="text-3xl font-bold text-primary">12</p>
        </div>
        <div className="border p-6 rounded-lg hover:border-primary transition cursor-pointer">
          <h3 className="font-bold mb-2">Reservas Pendientes</h3>
          <p className="text-3xl font-bold text-secondary">5</p>
        </div>
      </div>
    </div>
  </div>
);
