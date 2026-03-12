import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';
import { Plus, ListTree, Calculator, Search } from 'lucide-react';

export const ChartOfAccounts = () => {
  const [accounts, setAccounts] = useState<any[]>([]);

  useEffect(() => {
    const fetchAccounts = async () => {
      try {
        const response = await accountingService.getAccounts();
        setAccounts(response.data || []);
      } catch (error) {
        setAccounts([
          { id: '1105', name: 'Caja', type: 'Activo', balance: 450.00 },
          { id: '1110', name: 'Bancos / Wallet', type: 'Activo', balance: 2450.00 },
          { id: '4135', name: 'Ventas de Servicios', type: 'Ingreso', balance: 15200.00 },
          { id: '5105', name: 'Gastos de Personal', type: 'Egreso', balance: 2750.00 },
        ]);
      }
    };
    fetchAccounts();
  }, []);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
        <div className="flex items-center gap-3">
          <ListTree className="text-primary" size={24} />
          <h2 className="text-xl font-bold text-gray-800">Plan de Cuentas</h2>
        </div>
        <button className="bg-primary text-white px-4 py-2 rounded-lg flex items-center gap-2 text-sm font-bold hover:bg-blue-900 transition shadow-sm">
          <Plus size={18} /> Crear Cuenta
        </button>
      </div>

      <div className="p-4 bg-gray-50 flex gap-4 border-b border-gray-100">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-2.5 text-gray-400" size={16} />
          <input type="text" placeholder="Buscar cuenta por código o nombre..." className="w-full pl-10 pr-4 py-2 border rounded-lg text-sm outline-none" />
        </div>
        <select className="border rounded-lg px-4 text-sm outline-none bg-white">
          <option>Todos los tipos</option>
          <option>Activo</option>
          <option>Pasivo</option>
          <option>Patrimonio</option>
          <option>Ingreso</option>
          <option>Egreso</option>
        </select>
      </div>

      <table className="w-full text-left">
        <thead className="bg-gray-50 text-gray-500 text-xs uppercase font-bold">
          <tr>
            <th className="px-6 py-4">Código</th>
            <th className="px-6 py-4">Nombre de Cuenta</th>
            <th className="px-6 py-4">Tipo</th>
            <th className="px-6 py-4 text-right">Saldo Actual</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-100 text-sm">
          {accounts.map(acc => (
            <tr key={acc.id} className="hover:bg-gray-50 transition cursor-pointer group">
              <td className="px-6 py-4 font-mono font-bold text-primary">{acc.id}</td>
              <td className="px-6 py-4 font-medium text-gray-800">{acc.name}</td>
              <td className="px-6 py-4">
                <span className={`px-2 py-1 rounded text-[10px] font-bold uppercase ${
                  acc.type === 'Activo' ? 'bg-blue-100 text-blue-600' :
                  acc.type === 'Ingreso' ? 'bg-green-100 text-green-600' : 'bg-gray-100 text-gray-600'
                }`}>
                  {acc.type}
                </span>
              </td>
              <td className="px-6 py-4 text-right font-bold text-gray-900">${acc.balance.toLocaleString()} USD</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
