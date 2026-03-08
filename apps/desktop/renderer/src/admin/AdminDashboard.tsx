import React from 'react';

export const AdminDashboard = () => (
  <div className="space-y-8">
    <div className="bg-white p-8 rounded-lg shadow-sm">
      <h2 className="text-xl font-bold text-red-600 mb-6 uppercase tracking-widest">Torre de Control SARITA</h2>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
        <div className="p-6 bg-gray-50 rounded-lg">
          <p className="text-gray-500 text-xs font-bold uppercase">Total Usuarios</p>
          <p className="text-3xl font-bold">12,450</p>
        </div>
        <div className="p-6 bg-gray-50 rounded-lg">
          <p className="text-gray-500 text-xs font-bold uppercase">Negocios Activos</p>
          <p className="text-3xl font-bold">342</p>
        </div>
        <div className="p-6 bg-gray-50 rounded-lg">
          <p className="text-gray-500 text-xs font-bold uppercase">Alertas Sistema</p>
          <p className="text-3xl font-bold text-red-500">0</p>
        </div>
      </div>

      <div className="border-t pt-8">
        <h3 className="font-bold mb-4">Moderación de Nuevos Prestadores</h3>
        <div className="space-y-4">
          {[
            { name: 'Hotel Altillanura', date: 'Hace 2h', status: 'Pendiente' },
            { name: 'Guía Local Tours', date: 'Hace 5h', status: 'Pendiente' }
          ].map(req => (
            <div key={req.name} className="flex justify-between items-center p-4 bg-gray-50 rounded">
              <span>{req.name}</span>
              <div className="flex gap-2">
                <button className="bg-green-500 text-white px-3 py-1 rounded text-xs font-bold">Aprobar</button>
                <button className="bg-red-500 text-white px-3 py-1 rounded text-xs font-bold">Rechazar</button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  </div>
);
