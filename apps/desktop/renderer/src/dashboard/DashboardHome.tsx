import React from 'react';

export const DashboardHome = () => (
  <div className="space-y-8">
    <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
      {[
        { label: 'Reservas Hoy', value: '42', color: 'bg-blue-500' },
        { label: 'Ventas (24h)', value: '$1.25M', color: 'bg-green-500' },
        { label: 'Delivery Activo', value: '15', color: 'bg-purple-500' },
        { label: 'Nuevos Usuarios', value: '8', color: 'bg-orange-500' },
      ].map(stat => (
        <div key={stat.label} className="bg-white p-6 rounded-lg shadow-sm">
          <p className="text-gray-500 text-sm">{stat.label}</p>
          <p className="text-2xl font-bold mt-2">{stat.value}</p>
          <div className={`h-1 w-10 mt-4 rounded-full ${stat.color}`} />
        </div>
      ))}
    </div>

    <div className="bg-white p-8 rounded-lg shadow-sm min-h-[400px]">
      <h2 className="text-xl font-bold mb-6 text-primary">Actividad Reciente</h2>
      <div className="space-y-4 text-gray-600">
        <p>✓ Nueva reserva confirmada por Andrés V.</p>
        <p>✓ Pago recibido vía Wallet: $45.00 USD</p>
        <p>✓ Operador Llanos Grill activó nuevo menú.</p>
      </div>
    </div>
  </div>
);
