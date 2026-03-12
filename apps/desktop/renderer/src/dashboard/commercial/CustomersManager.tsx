import React, { useEffect, useState } from 'react';
import { commercialService } from './commercialService';
import { UserPlus, Search, Filter, Mail } from 'lucide-react';

export const CustomersManager = () => {
  const [customers, setCustomers] = useState<any[]>([]);

  useEffect(() => {
    const fetchCustomers = async () => {
      try {
        const response = await commercialService.getCustomers();
        setCustomers(response.data || []);
      } catch (error) {
        setCustomers([
          { id: '1', first_name: 'Andrés', last_name: 'Viajero', email: 'andres@example.com', purchases: 12, segment: 'VIP' },
          { id: '2', first_name: 'Laura', last_name: 'Exploradora', email: 'laura@example.com', purchases: 5, segment: 'Recurrente' },
        ]);
      }
    };
    fetchCustomers();
  }, []);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
        <h2 className="text-xl font-bold text-gray-800">Directorio de Clientes (CRM)</h2>
        <button className="bg-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-blue-900 transition">
          <UserPlus size={18} />
          Nuevo Cliente
        </button>
      </div>

      <div className="p-6 grid grid-cols-1 md:grid-cols-2 gap-4 border-b border-gray-100">
        <div className="relative">
          <Search className="absolute left-3 top-3 text-gray-400" size={18} />
          <input type="text" placeholder="Buscar por nombre o email..." className="w-full pl-10 pr-4 py-2 border rounded-lg outline-none focus:ring-2 ring-primary/20" />
        </div>
        <div className="flex gap-2">
          <button className="px-4 py-2 border rounded-lg flex items-center gap-2 text-gray-600 hover:bg-gray-50"><Filter size={18} /> Filtros</button>
          <button className="px-4 py-2 border rounded-lg text-gray-600 hover:bg-gray-50">Segmentos</button>
        </div>
      </div>

      <table className="w-full text-left">
        <thead className="bg-gray-50 text-gray-500 text-xs uppercase font-bold">
          <tr>
            <th className="px-6 py-4">Cliente</th>
            <th className="px-6 py-4">Segmento</th>
            <th className="px-6 py-4">Compras</th>
            <th className="px-6 py-4 text-right">Acciones</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-100 text-sm">
          {customers.map(c => (
            <tr key={c.id} className="hover:bg-gray-50 transition">
              <td className="px-6 py-4">
                <p className="font-bold text-gray-800">{c.first_name} {c.last_name}</p>
                <p className="text-gray-400 text-xs">{c.email}</p>
              </td>
              <td className="px-6 py-4">
                <span className={`px-3 py-1 rounded-full text-xs font-bold ${c.segment === 'VIP' ? 'bg-purple-100 text-purple-600' : 'bg-blue-100 text-blue-600'}`}>
                  {c.segment}
                </span>
              </td>
              <td className="px-6 py-4 font-medium">{c.purchases} reservas</td>
              <td className="px-6 py-4 text-right flex justify-end gap-2">
                <button className="p-2 text-primary hover:bg-blue-50 rounded-lg"><Mail size={16} /></button>
                <button className="text-primary font-bold hover:underline">Ver Historial</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
