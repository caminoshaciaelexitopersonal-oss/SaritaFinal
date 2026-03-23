import React, { useEffect, useState } from 'react';
import { commercialService } from './commercialService';
import { BadgeDollarSign, CreditCard, Wallet, Landmark } from 'lucide-react';

export const SalesManager = () => {
  const [sales, setSales] = useState<any[]>([]);

  useEffect(() => {
    const fetchSales = async () => {
      try {
        const response = await commercialService.getSales();
        setSales(response.data || []);
      } catch (error) {
        setSales([
          { id: 'S-101', customer: 'Andrés V.', total: 120.00, method: 'Wallet SARITA', date: '07 Mar 2026' },
          { id: 'S-102', customer: 'Marta L.', total: 85.50, method: 'Tarjeta', date: '07 Mar 2026' },
        ]);
      }
    };
    fetchSales();
  }, []);

  const getMethodIcon = (method: string) => {
    if (method.includes('Wallet')) return <Wallet size={16} className="text-blue-600" />;
    if (method.includes('Tarjeta')) return <CreditCard size={16} className="text-purple-600" />;
    return <Landmark size={16} className="text-gray-600" />;
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100">
      <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
        <h2 className="text-xl font-bold text-gray-800">Registro de Ventas</h2>
        <button className="bg-green-600 text-white px-4 py-2 rounded-lg font-bold hover:bg-green-700 transition">
          Nueva Venta Directa
        </button>
      </div>

      <table className="w-full text-left">
        <thead className="bg-gray-50 text-gray-500 text-xs uppercase font-bold">
          <tr>
            <th className="px-6 py-4">ID Venta</th>
            <th className="px-6 py-4">Cliente</th>
            <th className="px-6 py-4">Método</th>
            <th className="px-6 py-4 text-right">Total</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-100 text-sm">
          {sales.map(s => (
            <tr key={s.id} className="hover:bg-gray-50 transition">
              <td className="px-6 py-4 font-bold text-primary">{s.id}</td>
              <td className="px-6 py-4">
                <p className="font-medium">{s.customer}</p>
                <p className="text-xs text-gray-400">{s.date}</p>
              </td>
              <td className="px-6 py-4">
                <div className="flex items-center gap-2">
                  {getMethodIcon(s.method)}
                  <span>{s.method}</span>
                </div>
              </td>
              <td className="px-6 py-4 text-right font-bold text-gray-800">${s.total.toFixed(2)} USD</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
