import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';
import { Table, Search, Filter } from 'lucide-react';

export const GeneralLedger = () => {
  const [ledger, setLedger] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchLedger = async () => {
      try {
        const response = await accountingService.getJournalEntries();
        setLedger(response.data || []);
      } catch (error) {
        console.error('Error al cargar Libro Mayor real.');
      } finally {
        setLoading(false);
      }
    };
    fetchLedger();
  }, []);

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
      <div className="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
        <h2 className="text-xl font-bold text-gray-800">Libro Mayor (General Ledger)</h2>
      </div>

      <div className="p-6 overflow-x-auto">
        <table className="w-full text-left">
          <thead className="bg-gray-50 text-gray-500 text-xs uppercase font-bold">
            <tr>
              <th className="px-6 py-4">Fecha</th>
              <th className="px-6 py-4">Cuenta</th>
              <th className="px-6 py-4">Descripción</th>
              <th className="px-6 py-4">Débito</th>
              <th className="px-6 py-4">Crédito</th>
              <th className="px-6 py-4">Saldo</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100 text-sm">
            {ledger.map((entry, idx) => (
              <tr key={idx} className="hover:bg-gray-50 transition">
                <td className="px-6 py-4">{entry.fecha}</td>
                <td className="px-6 py-4 font-medium text-primary">{entry.codigo_cuenta}</td>
                <td className="px-6 py-4 text-gray-500">{entry.descripcion}</td>
                <td className="px-6 py-4 font-mono">{entry.naturaleza === 'DB' ? entry.monto : '-'}</td>
                <td className="px-6 py-4 font-mono">{entry.naturaleza === 'CR' ? entry.monto : '-'}</td>
                <td className="px-6 py-4 font-bold">$0.00</td>
              </tr>
            ))}
          </tbody>
        </table>
        {!loading && ledger.length === 0 && (
          <div className="text-center py-10 text-gray-400">No hay movimientos contables reales en el sistema.</div>
        )}
      </div>
    </div>
  );
};
