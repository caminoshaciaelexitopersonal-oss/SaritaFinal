import React, { useState } from 'react';
import { Store } from 'lucide-react';
import { POSInterface } from './commercial/POSInterface';

export const DashboardHome = () => {
  const [showPOS, setShowPOS] = useState(false);

  if (showPOS) {
    return (
      <div className="space-y-6">
        <div className="flex justify-between items-center">
          <h2 className="text-2xl font-bold text-gray-800 uppercase tracking-tight">Terminal Punto de Venta (POS)</h2>
          <button
            onClick={() => setShowPOS(false)}
            className="bg-gray-200 text-gray-700 px-4 py-2 rounded-lg font-bold hover:bg-gray-300 transition"
          >
            Volver al Dashboard
          </button>
        </div>
        <POSInterface />
      </div>
    );
  }

  return (
  <div className="space-y-8">
    <div className="flex justify-end mb-4">
        <button
          onClick={() => setShowPOS(true)}
          className="bg-primary text-white px-6 py-3 rounded-xl font-bold flex items-center gap-2 hover:bg-opacity-90 transition shadow-lg shadow-primary/20"
        >
          <Store size={20} /> Abrir Punto de Venta (POS)
        </button>
    </div>
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
};
