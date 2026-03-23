import React from 'react';

export const DeliveryManager = () => (
  <div className="space-y-6">
    <div className="bg-white p-8 rounded-lg shadow-sm">
      <h2 className="text-xl font-bold text-primary mb-4">Centro de Órdenes Delivery</h2>
      <div className="flex gap-4 mb-10">
        {['Pendientes (3)', 'En Cocina (2)', 'En Camino (1)', 'Entregados'].map(tab => (
          <button key={tab} className="px-6 py-2 rounded-full border text-sm hover:bg-gray-50 transition">{tab}</button>
        ))}
      </div>

      <div className="space-y-4">
        {[1021, 1022, 1023].map(id => (
          <div key={id} className="p-6 border rounded-lg flex justify-between items-center hover:shadow-md transition">
            <div>
              <p className="font-bold">Orden #{id}</p>
              <p className="text-sm text-gray-500">Cliente: Laura E. | Llanos Grill</p>
            </div>
            <button className="text-primary font-bold">Ver Detalles →</button>
          </div>
        ))}
      </div>
    </div>
  </div>
);
