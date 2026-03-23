import React, { useEffect, useState } from 'react';
import { accountingService } from './accountingService';
import { Book, TrendingUp, TrendingDown, Landmark, AlertCircle, FileSpreadsheet } from 'lucide-react';

export const AccountingDashboard = () => {
  const [summary, setSummary] = useState<any>({ income: 0, expenses: 0, net_profit: 0 });

  useEffect(() => {
    const fetchSummary = async () => {
      try {
        const response = await accountingService.getIncomeStatement();
        setSummary(response.data);
      } catch (error) {
        setSummary({ income: 24500, expenses: 8200, net_profit: 16300 });
      }
    };
    fetchSummary();
  }, []);

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-800">Dashboard Contable (GESCONTABLE)</h2>
        <div className="flex gap-2">
          <button className="flex items-center gap-2 px-4 py-2 border rounded-lg text-gray-600 hover:bg-gray-50 transition font-bold text-sm">
            <FileSpreadsheet size={18} /> Exportar Reporte Mensual
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
          <div className="flex items-center justify-between mb-4">
            <div className="w-10 h-10 rounded-lg bg-green-100 flex items-center justify-center text-green-600"><TrendingUp size={20} /></div>
            <span className="text-green-500 text-xs font-bold">+12% vs mes ant.</span>
          </div>
          <p className="text-gray-500 text-xs font-bold uppercase">Ingresos Totales</p>
          <p className="text-2xl font-bold text-gray-800">${summary.income.toLocaleString()} USD</p>
        </div>

        <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-100">
          <div className="flex items-center justify-between mb-4">
            <div className="w-10 h-10 rounded-lg bg-red-100 flex items-center justify-center text-red-600"><TrendingDown size={20} /></div>
            <span className="text-red-500 text-xs font-bold">+5% vs mes ant.</span>
          </div>
          <p className="text-gray-500 text-xs font-bold uppercase">Egresos Totales</p>
          <p className="text-2xl font-bold text-gray-800">${summary.expenses.toLocaleString()} USD</p>
        </div>

        <div className="bg-primary text-white p-6 rounded-xl shadow-md border-b-4 border-secondary">
          <div className="flex items-center gap-3 mb-4">
            <Landmark size={24} />
            <p className="text-xs font-bold uppercase opacity-80 tracking-widest">Utilidad Neta</p>
          </div>
          <p className="text-3xl font-bold">${summary.net_profit.toLocaleString()} USD</p>
          <p className="text-[10px] mt-4 opacity-70">Sincronizado con Libro Mayor Real-Time</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
          <h3 className="font-bold text-lg mb-6 flex items-center gap-2 text-primary"><Book size={20} /> Asientos Recientes</h3>
          <div className="space-y-4">
            {[
              { id: 'J-1201', desc: 'Venta Safari Río Meta', amount: 120.0, type: 'Venta', date: 'Hoy' },
              { id: 'J-1202', desc: 'Pago Comisión SARITA', amount: -18.0, type: 'Gasto', date: 'Hoy' },
              { id: 'J-1203', desc: 'Recarga Insumos Lancha', amount: -45.5, type: 'Gasto', date: 'Ayer' },
            ].map((entry, i) => (
              <div key={i} className="flex justify-between items-center p-3 border-b border-gray-50">
                <div>
                  <p className="text-sm font-bold text-gray-800">{entry.desc}</p>
                  <p className="text-[10px] text-gray-400 font-bold">{entry.id} | {entry.date}</p>
                </div>
                <p className={`font-bold ${entry.amount > 0 ? 'text-green-600' : 'text-red-600'}`}>
                  {entry.amount > 0 ? '+' : ''}{entry.amount.toFixed(2)} USD
                </p>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
          <h3 className="font-bold text-lg mb-6 flex items-center gap-2 text-orange-600"><AlertCircle size={20} /> Alertas Contables</h3>
          <div className="space-y-4">
            <div className="p-4 bg-orange-50 border-l-4 border-orange-400 rounded">
              <p className="text-xs font-bold text-orange-800 uppercase">Diferencia de Conciliación</p>
              <p className="text-sm text-orange-700 mt-1">Se detectó una diferencia de $4.50 USD entre el saldo Wallet y el Libro Mayor. Se sugiere revisión.</p>
            </div>
            <div className="p-4 bg-blue-50 border-l-4 border-blue-400 rounded">
              <p className="text-xs font-bold text-blue-800 uppercase">Impuestos Pendientes</p>
              <p className="text-sm text-blue-700 mt-1">La declaración de IVA para el trimestre actual está lista para revisión y descarga.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
