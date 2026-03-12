import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';
import { FilePlus2, ListFilter, ArrowRightLeft, Info } from 'lucide-react';

export const JournalEntries = () => {
  const [entries, setEntries] = useState<any[]>([]);

  useEffect(() => {
    const fetchEntries = async () => {
      try {
        const response = await accountingService.getJournalEntries();
        setEntries(response.data || []);
      } catch (error) {
        setEntries([
          { id: 'J-1201', date: '07 Mar 2026', desc: 'Venta de Tour Safari Río Meta', debit: '1110 - Wallet', credit: '4135 - Ventas', amount: 120.00, auto: true },
          { id: 'J-1202', date: '07 Mar 2026', desc: 'Suministros Oficina', debit: '5105 - Gastos', credit: '1105 - Caja', amount: 45.00, auto: false },
        ]);
      }
    };
    fetchEntries();
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-bold text-gray-800">Libro Diario y Asientos</h2>
        <div className="flex gap-2">
          <button className="bg-gray-900 text-white px-4 py-2 rounded-lg flex items-center gap-2 text-sm font-bold hover:bg-black transition">
            <FilePlus2 size={18} /> Nuevo Asiento Manual
          </button>
        </div>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <table className="w-full text-left">
          <thead className="bg-gray-50 text-gray-500 text-xs uppercase font-bold border-b border-gray-100">
            <tr>
              <th className="px-6 py-4 w-32">Fecha</th>
              <th className="px-6 py-4">Descripción / Referencia</th>
              <th className="px-6 py-4">Cuentas (Debe / Haber)</th>
              <th className="px-6 py-4 text-right">Monto</th>
              <th className="px-6 py-4 text-center">Modo</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100 text-sm">
            {entries.map(e => (
              <tr key={e.id} className="hover:bg-gray-50/50 transition">
                <td className="px-6 py-4 text-gray-400 font-medium">{e.date}</td>
                <td className="px-6 py-4">
                  <p className="font-bold text-gray-800">{e.desc}</p>
                  <p className="text-[10px] text-primary uppercase font-bold">{e.id}</p>
                </td>
                <td className="px-6 py-4">
                  <div className="flex flex-col gap-1">
                    <span className="text-[11px] font-bold text-green-600">D: {e.debit}</span>
                    <span className="text-[11px] font-bold text-red-500">H: {e.credit}</span>
                  </div>
                </td>
                <td className="px-6 py-4 text-right font-mono font-bold text-gray-900">
                  ${e.amount.toFixed(2)}
                </td>
                <td className="px-6 py-4 text-center">
                  <span className={`px-2 py-0.5 rounded-full text-[9px] font-bold ${e.auto ? 'bg-blue-100 text-blue-600' : 'bg-gray-100 text-gray-500'}`}>
                    {e.auto ? 'SISTEMA' : 'MANUAL'}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="p-4 bg-primary/5 rounded-lg border border-primary/10 flex items-start gap-3">
        <Info className="text-primary mt-0.5" size={18} />
        <p className="text-xs text-primary/80 font-medium leading-relaxed">
          Generación Automática: El sistema registra automáticamente ingresos por Ventas, Reservas Confirmadas y Pedidos de Delivery,
          así como cargos por Comisiones y Retiros de Wallet.
        </p>
      </div>
    </div>
  );
};
